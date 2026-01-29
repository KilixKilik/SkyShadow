/* UI and Net Logic */
// kilixkilik

const TARGET_IP = "192.168.2.200";
const TARGET_PORT = 1344;

const _m = [83, 107, 121, 83, 104, 97, 100, 111, 119, 32, 67, 114, 101, 97, 116, 101, 32, 98, 121, 32, 107, 105, 108, 105, 120, 107, 105, 108, 105, 107, 46];

function showInfo() {
    Java.perform(() => {
        const Toast = Java.use("android.widget.Toast");
        const App = Java.use("android.app.ActivityThread").currentApplication();
        const context = App.getApplicationContext();
        const msg = String.fromCharCode.apply(null, _m);

        Java.scheduleOnMainThread(() => {
            Toast.makeText(context, msg, 1).show();
        });
    });
}

const connect_ptr = Module.findExportByName("libc.so", "connect");

Interceptor.attach(connect_ptr, {
    onEnter: function (args) {
        const sockaddr_p = args[1];
        if (sockaddr_p.readU16() === 2) {
            const port = sockaddr_p.add(2).readU16();
            if (port === 20480 || port === 47873) { // 80, 443
                sockaddr_p.add(2).writeU16((TARGET_PORT << 8) | (TARGET_PORT >> 8));
                const p = TARGET_IP.split('.').map(Number);
                const newAddr = (p[3] << 24) | (p[2] << 16) | (p[1] << 8) | p[0];
                sockaddr_p.add(4).writeU32(newAddr);
            }
        }
    }
});

showInfo();

// kilixkilik
