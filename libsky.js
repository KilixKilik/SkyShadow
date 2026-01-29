// kilixkilik

const ip = "192.168.2.200";
const p = 1344;

const t_l = [
    "nekkimobile.ru", "shadowfight2.com", "nekki.com",
    "appsflyer.com", "facebook.com", "tapjoy.com",
    "95.213.140.21", "51.195.27.140", "51.195.27.146"
];
=
function si() {
    setTimeout(() => {
        Java.perform(() => {
            const T = Java.use("android.widget.Toast");
            const AT = Java.use("android.app.ActivityThread");
            const ctx = AT.currentApplication().getApplicationContext();
            Java.scheduleOnMainThread(() => {
                T.makeText(ctx, "SkyShadow Create by kilixkilik.", 1).show();
            });
        });
    }, 5000);
}

const gai = Module.findExportByName("libc.so", "getaddrinfo");
Interceptor.attach(gai, {
    onEnter: function (a) {
        this.n = a[0].readUtf8String(); // get hostname
    },
    onLeave: function (r) {
        if (this.n && t_l.some(t => this.n.includes(t))) {
        }
    }
});

const cp = Module.findExportByName("libc.so", "connect");
Interceptor.attach(cp, {
    onEnter: function (a) {
        const sa = a[1]; // sockaddr
        if (sa.readU16() === 2) { // AF_INET
            const pr = sa.add(2).readU16();
            // Redirect all targets
            sa.add(2).writeU16((p << 8) | (p >> 8)); // port
            const pt = ip.split('.').map(Number);
            const na = (pt[3] << 24) | (pt[2] << 16) | (pt[1] << 8) | pt[0];
            sa.add(4).writeU32(na); // ip
        }
    }
});

si(); // start toast
