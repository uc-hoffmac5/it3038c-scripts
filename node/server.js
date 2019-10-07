var http = require ("http")
var fs = require("fs")
var os = require("os")
var ip = require("ip")

http.createServer(function(req, res){
    if(req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err,body){
            res.writeHead(200, {"content-Type": "text.html"})
            res.end(body)
        })
        }
        else if (req.url.match("/sysinfo")) {
            myHostName=os.hostname();
            myServerUptime=process.uptime()
            Days= Math.floor(myServerUptime/86400)
            Hours=Math.floor(myServerUptime/3600)
            Minutes=Math.floor(myServerUptime/60)
            Seconds= Math.floor(myServerUptime)
            myTotalMemory=os.totalmem/1048576
            myFreeMemory=os.freemem/1048576
            myCPUCount=os.cpus().length
            html=`
            <!DOCTYPE HTML>
            <HTML>
                <HEAD>
                    <title> NodeJS SysInfo </title>
                </head>
                <body>
                <p> Hostname: ${myHostName} </p>
                <p> IP: ${ip.address()}</p>
                <p> Server Uptime: Days ${Days}, Hours ${Hours}, Minutes:${Minutes}, Seconds: ${Seconds} </p>
                <p> Total Memory: ${myTotalMemory}MB</p>
                <p> Free Memory: ${myFreeMemory}MB </p>
                <p> CPUs: ${myCPUCount} </p>
                </body>
            </html>`
            res.writeHead(200, {"Content-Type": "text/html"})
            res.end(html)
        }   

        else {
            res.writeHead(404, {"Content-Type": "text/plain:"})
            res.end("404 file not found")
        }
}).listen(3000)

console.log("Server Listening on port 3000")