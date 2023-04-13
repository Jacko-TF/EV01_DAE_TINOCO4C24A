from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'pago/login.html')

def loguear(request):
    usuario= request.POST['usuario']
    contraseña= request.POST['password']

    if(usuario=='tinoco' and contraseña=='123'):
        return render(request, 'pago/formulario.html')
    else:
        context = { 'mensaje':'Nombre de usuario o contraseña incorrectos' }
        return render(request, 'pago/login.html', context)
    
def enviar(request):
    horas_trabajadas = int(request.POST['horas'])
    pago_hora = float(request.POST['pago_hora'])

    if(horas_trabajadas>48):
        horas_extra = horas_trabajadas-48
        sueldo_neto = (48*pago_hora)+(horas_extra*2*pago_hora)+50
    else:
        horas_extra = 0
        sueldo_neto = (horas_trabajadas*pago_hora)+50

    context = {
        'horas':horas_trabajadas,
        'pago_hora':pago_hora,
        'horas_extra': horas_extra,
        'sueldo_neto': sueldo_neto,
    }
    return render(request, 'pago/respuesta.html', context)