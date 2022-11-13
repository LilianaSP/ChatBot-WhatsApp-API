//Paquetes que vienen con Node
const fs = require('fs');
const ora = import('ora');
const chalk = import('chalk')
const puppeteer = require('puppeteer');

//Variable para importar nuestra base de datos
var mysql = require('mysql2');

//Creamos la vinulación con el servidor de whatsapp
const { Client, LocalAuth, MessageMedia } = require('whatsapp-web.js');
//Gener el código QR para poder escanearlo con el celular
const qrcode = require('qrcode-terminal');
const { castImmutable } = require('immer');

//Funciones para guardar nuestra sesión y poder reutilizarla en el servidor
let client;
let sessionData;

console.log('No existe una sesión iniciada');

client = new Client(
);



//Genera el código QR
client.on('qr', (qr) => {
    qrcode.generate(qr, { small: true });
});

//Se ejecuta cuando se a vinculado la sesión, es decir cuando sale el mensaje de que el cliente esta listo
client.on('authenticated', (session) => {
});

//Se ejecuta cuando el cliente esta listo
client.initialize();

client.on('ready', () => {
    console.log('Client is ready')
    listenMessage()
})

var conexion = mysql.createConnection({
    host: "localhost",
    user: "root",   
    password: "",
    database: "Nenis"
});

conexion.connect(function(error){
    if(error){
        throw error;
    }else{
        console.log("Conexion exitosa con la base de datos");
    }
})

//Función para imprimir la base de datos de la tabla de productos
conexion.query('SELECT * FROM producto', function(error,results, fields){
    if(error)
    throw error;
    results.forEach(result => {
        console.log(result)
    });
})

//Función para registrar datos en la tabla de cliente
//conexion.query('INSERT INTO cliente(nombre, telefono) VALUES ("Ximena M.", "333126457")', function(error,results){
    //if(error) throw error;
    //console.log("Registro agregado con exito", results);
//});



//Función para actualizar datos en la tabla de pedido
//conexion.query('INSERT INTO producto_pedido(cantidad) VALUES ("4")', function(error,results){
    //if(error) throw error;
    //console.log("Pedido creado exitosamente", results);
//});




// Esta funcion se encarga de escuchar cada vez que entra un mensaje nuevo
const listenMessage = () => {
    client.on('message', (msg => {
        const {from, to, body} = msg;

        //let firstMenu = "*This is a test message*\nTesting how to formatt a message.\tLOL."
        client.sendMessage(to, "")

        switch(body){
            case '1':
            sendMessage(from, "Caso 1\n.*Aquí iría nuestra base de datos del producto*")
            sendMedia(from, 'pastelitos.jpg')
            break;

            case '2':
            sendMessage(from, "Caso 2\n.*Aquí iría la base de datos del pedido*")
            break;

            case '3':
            sendMessage(from, "Caso 3\n.*Agenda tu cita, Zona metropolitana*")
            sendMedia(from, 'Citas/Cita 1 Zapopan.ics')
            break;

            case '4':
            sendMessage(from, "Caso 4")
            sendMessage(from, "*Aquí iría la base de datos de Pedido par confirmarlo*")
            break;

            case '5':
            sendMessage(from, "Caso 5")
            sendMessage(from, "*Gracias por contactarnos!*\n Esperemos haberte ayudado.")
            break;

            default:
            sendMessage(from, "*Gracias por contactarnos!*\nSomos una empresa dedicada a la venta de pastelitos para todo tipo de ocasiones.\n\n*¿En qué podemos ayudarte?*\n1. Pastelitos de temporada\n2. Mis pedidos\n3. Agendar entrega\n4.Confirmar pedido\n5. Salir")

            break;
        }

        console.log(from, to, body)
    }))
}

//Función para enviar archivos
const sendMedia = (to, file) => {
    const mediaFile = MessageMedia.fromFilePath(`./media/${file}`)
    client.sendMessage(to, mediaFile)
}

//Función para enviar mensajes
const sendMessage = (to, message) => {
    client.sendMessage(to, message)
}


conexion.end();
