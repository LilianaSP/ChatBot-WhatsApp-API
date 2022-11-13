//Paquetes que vienen con Node
const fs = require('fs');
//const ora = require('ora');
const chalk = require('chalk')


//Creamos la vinulación con el servidor de whatsapp
const { Client } = require('whatsapp-web.js');
//Gener el código QR para poder escanearlo con el celular
const qrcode = require('qrcode-terminal');

//Funciones para guardar nuestra sesión y poder reutilizarla en el servidor
const SESSION_FILE_PATH = './session.json';
let client;
let sessionData;

const withSession = () => {
    //Si existe el archivo de sesión, lo cargamos
    //Creamos un spinner para que se vea que se está cargando
    const spinner = ora(`Cargando ${chalk.yellow('Valididando session con WhatsApp...')}`);
    sessionData = require(SESSION_FILE_PATH);
    spinner.start();
    client = new Client({
        session: sessionData
    })

    client.on('ready', () => {
        console.log('Client is ready!');
        spinner.stop();
    }) 

}

//Esta función genera el qr code
const withOutSession = () => {
    console.log('No existe una sesión iniciada');

    client = new Client();

    //Genera el código QR
    client.on('qr', (qr) => {
        qrcode.generate(qr, { small: true });
    });

    //Se ejecuta cuando se a vinculado la sesión, es decir cuando sale el mensaje de que el cliente esta listo
    client.on('authenticated', async (session) => {
        //Guardamos las credenciales de la sesión
        sessionData = session;
        // console.log(session)
        fs.writeFile(SESSION_FILE_PATH, "Its Working Iker tqm", (err) =>  {
            if (err) {
                console.log(err);
            }
        });
    });

    //Se ejecuta cuando el cliente esta listo
    client.initialize();
}

(fs.existsSync(SESSION_FILE_PATH)) ? withSession() : withOutSession();