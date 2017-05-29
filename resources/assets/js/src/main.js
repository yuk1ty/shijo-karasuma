// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.config.productionTip = false
Vue.use(VueAxios, axios)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})

"use static";
!function() {
    function i(i, t) {
        function n(i) {
            s.x = i.pageX - window.innerWidth / 2,
            s.y = i.pageY - window.innerHeight / 2
        }
        function e(i) {
            s.x = Math.min(Math.max(-i.gamma, -30), 30) * (window.innerWidth / 30),
            s.y = Math.min(Math.max(-i.beta, -30), 30) * (window.innerHeight / 30)
        }
        var o = this;
        void 0 === t && (t = {}),
        this.options = {
            directionX: 0,
            directionY: -1,
            velocityX: [.1, .2],
            velocityY: [.13, .4],
            bounceX: !0,
            bounceY: !1,
            parallax: .11,
            pivot: 0,
            density: 4601,
            dotRadius: [1, 3.6],
            linkColor: "rgba(254,123,211,0.25)",
            linkDistance: 50,
            linkWidth: 1.8,
            backgroundColor: "rgba(250,250,250,0.5)"
        };
        var i = "string" == typeof i || i instanceof String ? document.getElementById(i) : i;
        if ("CANVAS" == i.tagName) {
            for (var a in t)
                this.options[a] = t[a];
            t = this.options;
            var r, d, l, c = this._ctx = i.getContext("2d", {
                alpha: !t.backgroundColor
            }), s = {
                x: 0,
                y: 0
            }, m = function() {
                t.backgroundColor ? (c.fillStyle = t.backgroundColor,
                c.fillRect(0, 0, d, l),
                c.fillStyle = t.dotColor) : c.clearRect(0, 0, d, l),
                c.beginPath();
                for (var i, n, e, o = 0; o < r.length; o++) {
                    if (i = r[o],
                    i.x += i.vx,
                    i.y += i.vy,
                    t.parallax) {
                        var a = i.z * t.parallax;
                        i.dx += (s.x * a - i.dx) / 10,
                        i.dy += (s.y * a - i.dy) / 10
                    }
                    n = i.x + i.dx,
                    e = i.y + i.dy,
                    (0 > n || n > d) && (t.bounceX ? i.vx = -i.vx : i.x = (n + d) % d - i.dx),
                    (0 > e || e > l) && (t.bounceY ? i.vy = -i.vy : i.y = (e + l) % l - i.dy),
                    c.moveTo(n + i.r, e),
                    c.arc(n, e, i.r, 0, 2 * Math.PI);
                    for (var h = o - 1; h >= 0; h--) {
                        var w = r[h]
                          , v = w.x - i.x
                          , y = w.y - i.y
                          , u = Math.sqrt(v * v + y * y);
                        if (u < t.linkDistance) {
                            var n = i.x + i.dx
                              , e = i.y + i.dy
                              , f = w.x + w.dx
                              , x = w.y + w.dy
                              , g = Math.atan2(x - e, f - n)
                              , p = Math.cos(g)
                              , M = Math.sin(g);
                            n += i.r * p,
                            e += i.r * M,
                            f -= w.r * p,
                            x -= w.r * M,
                            c.moveTo(n, e),
                            c.lineTo(f, x)
                        }
                    }
                }
                c.stroke(),
                t.dotColor && c.fill(),
                requestAnimationFrame(m)
            }, h = this._refresh = function() {
                r = o._ = o._ || [];
                var n = [].concat(t.dotRadius);
                n[0] == n[1] && (n = n[0]),
                d = i.width = i.offsetWidth,
                l = i.height = i.offsetHeight;
                for (var e = t.velocityX, a = t.velocityY, s = Math.random, m = Math.ceil(d * l / t.density), h = r.length - 1; h >= 0; h--)
                    (r[h].x > d || r[h].y > l) && r.splice(h, 1);
                for (m < r.length && r.splice(m); m > r.length; ) {
                    var w = s();
                    r.push({
                        z: (w - t.pivot) / 4,
                        r: n[1] ? w * (n[1] - n[0]) + n[0] : n[0],
                        x: Math.ceil(s() * d),
                        y: Math.ceil(s() * l),
                        vx: (t.directionX || (s() > .5 ? 1 : -1)) * (s() * (e[1] - e[0]) + e[0]),
                        vy: (t.directionY || (s() > .5 ? 1 : -1)) * (s() * (a[1] - a[0]) + a[0]),
                        dx: 0,
                        dy: 0
                    })
                }
                c.strokeStyle = t.linkColor,
                c.lineWidth = t.linkWidth,
                c.fillStyle = t.dotColor
            }
            ;
            window.addEventListener("resize", h, !1),
            document.addEventListener("mousemove", n, !1),
            window.addEventListener("deviceorientation", e, !1),
            h(),
            m()
        }
    }
    new i("zodiac")
}(),
function() {
    for (var i = 0, t = ["ms", "moz", "webkit", "o"], n = 0; n < t.length && !window.requestAnimationFrame; ++n)
        window.requestAnimationFrame = window[t[n] + "RequestAnimationFrame"],
        window.cancelAnimationFrame = window[t[n] + "CancelAnimationFrame"] || window[t[n] + "CancelRequestAnimationFrame"];
    window.requestAnimationFrame || (window.requestAnimationFrame = function(t) {
        var n = (new Date).getTime()
          , e = Math.max(0, 16 - (n - i))
          , o = window.setTimeout(function() {
            t(n + e)
        }, e);
        return i = n + e,
        o
    }
    ),
    window.cancelAnimationFrame || (window.cancelAnimationFrame = function(i) {
        clearTimeout(i)
    }
    )
}();
