from aiohttp import web
import senha

async def handle(request):
    valor = request.match_info.get('name', '')
    if senha.verifica_forca_senha(valor):
        text = "Senha Forte: " + valor
    else:
        text = "Senha Fraca: " + valor
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app)
