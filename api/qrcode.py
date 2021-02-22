from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):

    #generate a qr code based on the value provided in url path
    def qr_code_generator(self, data, fill, back):
        import qrcode
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_Q,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        image = qr.make_image(fill_color=fill, back_color=back)
        image.save('portfolio.png')

    def do_GET(self):
        user_path = self.path
        parse_path = dict(parse.parse_qsl(parse.urlsplit(user_path).query))
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        qr_code_generator("https://ai-pree.github.io/Portfolio/", "black", "white");

        if ["data", "fill", "background" in parse_path:
            message = parse_path["data"] + "\n" + parse_path["fill"] 
        else:
            message = "Hello, stranger!"        
        
        self.wfile.write(message.encode())
        return