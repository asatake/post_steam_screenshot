const electron = require("electron");
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
let mainWindow;

const WIDTH = 400;
const HEIGHT = 300;

app.on('window-all-closed', function() {
    app.quit();
});

app.on('ready', function() {
    var subpy = require('child_process').spawn('python', ['app.py']);
    var rq = require('request-promise');
    var mainAddr = 'http://localhost:5000';

    var openWindow = function() {
        mainWindow = new BrowserWindow({ width: WIDTH, height: HEIGHT });
        mainWindow.loadURL(mainAddr);

        mainWindow.on('closed', function() {
            mainWindow = null;
            subpy.kill('SIGINT');
        });
    };

    var startUp = function() {
        rq(mainAddr)
            .then(function(htmlString) {
                console.log('server started.');
                openWindow();
            })
            .catch(function(err) {
                startUp();
            });
    };

    startUp();
});
