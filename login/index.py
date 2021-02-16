#importar as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import dataBaser           

#Criar nossa janela
jan = Tk() # atribuindo que a variavel é uma janela
jan.title('DP Systems - Acess Panel') # Titulo da janela
jan.geometry('600x300') # Tamanho da janela
jan.configure(background='white') # Cor da janela
jan.resizable(width=False, height=False) # com esse comando impedimos que mudem o tamanho da janela
jan.attributes('-alpha', 0.9) # Colocar transparencia na Janela, não é obrigatorio.
jan.iconbitmap(default = 'icons/Logoicon.ico') # tem que estar em .ico

# ===== CARREGANDO IMAGENS ======
logo = PhotoImage(file="icons/logo.png") # Cria a variavel com a imagem

# ===== WIDGET DA JANELA ====
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
#Aqui configuramos o Frame da esquerda... bg = cor, relief = conf padroes
LeftFrame.pack(side=LEFT) # aparecer do lado esquerdo

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
#Aqui configuramos o Frame da direita... bg = cor, relief = conf padroes
RightFrame.pack(side=RIGHT) # aparecer do lado direito

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE") # Inserindo imageem do lado esquerdo
LogoLabel.place(x=50, y=100) # Posicionamento da imagem

UserLabel = Label(RightFrame, text="Username:", font=("Century Gotic", 20), bg="MIDNIGHTBLUE", fg='white') # Inserindo textos do lado direito, fg é a cor do texto.
UserLabel.place(x=5, y=100) # posicionamento do texto

UserEntry = ttk.Entry(RightFrame, width=30) # Caixa de entrada de dados
UserEntry.place(x=155, y=113) # Posicionamento da caixa, sendo X posição em relação a lateral e Y em relação a altura

PassLabel = Label(RightFrame, text="Password:", font=("Century Gotic", 20), bg="MIDNIGHTBLUE", fg='white') # Inserindo textos do lado direito, fg é a cor do texto.
PassLabel.place(x=5, y=150) # posicionamento do texto

PassEntry = ttk.Entry(RightFrame, width=30, show='*') # Caixa de entrada de dados
PassEntry.place(x=155, y=160) # Posicionamento da caixa, sendo X posição em relação a lateral e Y em relação a altura

# ==== Criando Botões =====

def Login():
    User = UserEntry.get() # Pega os dados informados
    Pass = PassEntry.get() # Pega os dados informados

    dataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """, (User, Pass)) # Pega os dados no Database
    print('Selecionou')
    VerifyLogin = dataBaser.cursor.fetchone() # Verifica se existe (pode ser fetchall, fetchone, fetchmany())
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title='Login Info', message='Acesso Confirmado. Bem Vindo!')
    except:
        messagebox.showinfo(title='Login Info', message='Acesso negado. Verifique se esta cadastrado no sistema!')

LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login) # Cria o botao
LoginButton.place(x=155, y=220) # Posicionamento do botao

def Register(): # Funcao criada para executar no botao Register
    # Removendo os botoes de login:
    LoginButton.place(x=5000) # muda a posição do botao
    RegisterButton.place(x=5000) # muda a posição do botao
    #Inserindo botoes de cadastro:
    NomeLabel = Label(RightFrame, text='Nome:', font=("Century Gotic", 20), bg='MIDNIGHTBLUE', fg='white') # Inserindo textos do lado direito, fg é a cor do texto.
    NomeLabel.place(x=5, y=5) # Posicionamento do texto
    NomeEntry = ttk.Entry(RightFrame, width=40) # Caixa de entrada de texto
    NomeEntry.place(x=100, y=15) # posicionamento da caixa

    EmailLabel = Label(RightFrame, text='Email:', font=("Century Gotic", 20), bg="MIDNIGHTBLUE", fg='white') # Inserindo textos do lado direito, fg é a cor do texto.
    EmailLabel.place(x=5, y=40) # POsicionamento do texto
    EmailEntry = ttk.Entry(RightFrame, width=40) # Caixa de entrada do texto
    EmailEntry.place(x=100, y=50) # posicionamento da caixa
    
    def Registertodb(): # Funcao criada para executar a inserção no Bando de Dados
        Name = NomeEntry.get() # pega os dados inseridos
        Email = EmailEntry.get() # pega os dados inseridos
        User = UserEntry.get() # pega os dados inseridos
        Pass = PassEntry.get() # pega os dados inseridos
        
        if (Name == '' or Email == '' or User == '' or Pass == ''): # Valida se todos os campos foram digitados
            messagebox.showerror(title='Register Error', message='Preencha todos os campos.') # mensagem de erro
        else: # se estiver tudo OK ele grava no banco de dados.
            dataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Pass)) # Insere os dados nos valores da tabela
            dataBaser.conn.commit() # Salva no banco de dados
            messagebox.showinfo(title="Register Info", message="Conta criada com sucesso") # Mostra pop-up com msn

    Register = ttk.Button(RightFrame, text="Register", width=30, command=Registertodb) # criacao do botao com comando
    Register.place(x=155, y=220) # posicionamento do botao

    def BackToLogin(): # Funcao criada para executar no botao Back
        # Removendo os botoes de registro:
        NomeLabel.place(x=5000) # posicionamento do texto, tira da tela
        NomeEntry.place(x=5000) # posicionamento da caixa de texto, tira da tela
        EmailLabel.place(x = 5000) # posicionamento do texto, tira da tela
        EmailEntry.place(x=5000) # posicionamento da caixa de texto, tira da tela
        Register.place(x=5000) # posicionamento do botao, tira da tela
        BackButton.place(x=5000) # posicionamento do botao, tira da tela
        #Trazendo de volta os botoes de login:
        LoginButton.place(x=155) # Posicionamento do botao, traz de volta a tela
        RegisterButton.place(x=185) # Posicionamento do botao, traz de volta a tela

    BackButton = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin) # criacao do botao com comando
    BackButton.place(x=185, y=260) # Posicionamento do botao


RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register) # criacao do botao com comando
RegisterButton.place(x=185, y=260) # posicionamento do botao


jan.mainloop() # informa que as propiedades da janela acabou.. daqui para baixo nao entra mais na janela



