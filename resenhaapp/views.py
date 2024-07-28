from django.shortcuts import render,redirect,HttpResponse
from .models import leituras
from .forms import leiturasform
from django.contrib.auth.decorators import login_required


def livro(request):
    dados = {
        'dados': leituras.objects.all()
    }
    return render(request,'resenhas/filmes.html',context=dados)

def detalhe(request,id_filme):
    dados = {
        'dados': leituras.objects.get(pk=id_filme)
    }
    return render(request,'resenhas/detalhe.html',dados)

@login_required
def criar(request):
    if request.method == 'POST':
        leitura_form = leiturasform(request.POST)
        if leitura_form.is_valid():
            leitura_form.save()
        return redirect('filmes')
    else:
        leitura_form = leiturasform()
        formulario = {
            'formulario': leitura_form
        }
        return render(request,'resenhas/novo_filme.html',context = formulario)

@login_required   
def editar(request,id_filme):
    resenha = leituras.objects.get(pk=id_filme)
    if request.method == 'GET':
        formulario = leiturasform(instance=resenha)
        return render(request,'resenhas/novo_filme.html',{'formulario': formulario})
    else:
        formulario = leiturasform(request.POST,instance=resenha)
        if formulario.is_valid():
            formulario.save()
        return redirect('filmes')

@login_required   
def excluir(request,id_filme):
    resenha = leituras.objects.get(pk=id_filme)
    if request.method == 'POST':
        resenha.delete()
        return redirect('filmes')
    return render(request,'resenhas/confirmar_exclusao.html',{'item':resenha})