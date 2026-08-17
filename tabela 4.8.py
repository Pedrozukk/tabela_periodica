import tkinter as tk
from tkinter import messagebox

elements = {
            'H': "Hidrogênio; 1; 1.008 de massa\nNormalmente encontrado no estado gasoso; Curiosidade: auxilia na fotossíntese",
            'He': "Hélio; 2; 4.003 de massa\nNormalmente encontrado no estado gasoso; Curiosidade: ótimo em atividades criogênicas",
            'Li': "Lítio; 3; 6.941 de massa\nNormalmente encontrado no estado sólido; Curiosidade: utilizado em baterias",
            'Be': "Berílio; 4; 9.012 de massa \normalmente encontrado no estado sólido; Curiosidade: utilizado em reatores nucleares, raio-x, espelhos e aeronaves, entre outras coisas",
            'B': "Boro; 5; 10.811 de massa \nNormalmente encontrado no estado sólido; Curiosidade: transporte de açúcar e auxilia no metabolismo",
            'C': "Carbono; 6; 12.011 de massa \nNormalmente encontrado no estado sólido; Curiosidade: produção de energia, e fórmula química do diamante",
            'N': "Nitrogênio; 7; 14.007 de massa \nNormalmente encontrado no estado gasoso; Curiosidade: responsável pelo crescimento vegetativo",
            'O': "Oxigênio; 8; 15.999 de massa \nNormalmente encontrado no estado gasoso; Curiosidade: essencial para a vida",
            'F': "Flúor; 9; 18.998 de massa \nNormalmente encontrado no estado sólido; Curiosidade: energia nuclear", 
            'Ne': "Neônio; 10; 20.18 de massa \nNormalmente encontrado no estado gasoso; Curiosidade: sob baixas pressões, o gás emite uma luz brilhante em várias tonalidades",
            'Na': "Sódio; 11; 22.99 de massa \nNormalmente encontrado no estado sólido; Curiosidade: pode entrar em combustão espontânea quando entra em contato com a água",
            'Mg': "Magnésio; 12; 24.305 de massa \nNormalmente encontrado no estado sólido; Curiosidade: atua na contração dos músculos",
            'Al': "Alumínio; 13; 26.982 de massa \nNormalmente encontrado no estado sólido; Curiosidade: não é encontrado pronto na natureza",
            'Si': "Silício; 14; 28.086 de massa \nNormalmente encontrado no estado sólido; Curiosidade: representa 25,7% da crosta terrestre",
            'P': "Fósforo; 15; 30.974 de massa \nNormalmente encontrado no estado sólido; Curiosidade: altamente reativo quando exposto à atmosfera", 
            'S': "Enxofre; 16; 32.065 de massa \nNormalmente encontrado no estado sólido; Curiosidade: pode ser encontrado em depósitos vulcânicos ou sedimentares",
            'Cl': "Cloro; 17; 35.453 de massa \nNormalmente encontrado no estado gasoso; Curiosidade: é responsável por 2,9% do oceano",
            'Ar': "Argônio; 18; 39.948 de massa \nNormalmente encontrado no estado gasoso; Curiosidade: serve como proteção em soldas",
            'K': "Potássio; 19; 39.098 de massa \nNormalmente encontrado no estado sólido; Curiosidade: sétimo elemento mais presente na crosta terrestre",
            'Ca': "Cálcio; 20; 40.078 de massa \nNormalmente encontrado no estado sólido; Curiosidade: auxilia no crescimento e conservação dos ossos",
            'Sc': "Escândio; 21; 44.956 de massa \nNormalmente encontrado no estado sólido; Curiosidade: composição de aviões de guerra",
            'Ti': "Titânio; 22; 47.867 de massa \nNormalmente encontrado no estado sólido; Curiosidade: é utilizado em peças para motores",
            'V': "Vanádio; 23; 50.942 de massa \nNormalmente encontrado no estado sólido; Curiosidade: auxilia a combater a diabetes",
            'Cr': "Cromo; 24; 51.996 de massa \nNormalmente encontrado no estado sólido; Curiosidade: muito resistente à corrosão e ataque químico em temperatura ambiente",
            'Mn': "Manganês; 25; 54.938 de massa \nNormalmente encontrado no estado sólido; Curiosidade: essencial na formação óssea",
            'Fe': "Ferro; 26; 55.845 de massa \nNormalmente encontrado no estado sólido; Curiosidade: um dos elementos mais abundantes na Terra",
            'Co': "Cobalto; 27; 58.993 de massa \nNormalmente encontrado no estado sólido; Curiosidade: utilizado na indústria de tinta e cerâmica para a produção de pigmentos branco e azul",
            'Ni': "Níquel; 28; 58.693 de massa \nNormalmente encontrado no estado sólido; Curiosidade: utilizado na cunhagem de moedas",
            'Cu': "Cobre; 29; 63.546 de massa \nNormalmente encontrado no estado sólido; Curiosidade: primeiro metal trabalhado pelo homem",
            'Zn': "Zinco; 30; 65.409 de massa \nNormalmente encontrado no estado sólido; Curiosidade: bastante utilizado em ligas metálicas",
            'Ga': "Gálio; 31; 69.723 de massa \nNormalmente encontrado no estado líquido; Curiosidade: utilizado como um semicondutor", 
            'Ge': "Germânio; 32; 72.64 de massa \nNormalmente encontrado no estado sólido; Curiosidade: catalizador da fabricação de plástico PET na fabricação de garrafas",
            'As': "Arsênio; 33; 74.922 de massa \nNormalmente encontrado no estado sólido; Curiosidade: extremamente tóxico para os seres humanos, quando em sua forma inorgânica",
            'Se': "Selênio; 34; 78.96 de massa \nNormalmente encontrado no estado sólido; Curiosidade: tem uma importante ação no corpo do ser humano, que é a ação antioxidante",
            'Br': "Bromo; 35; 79.904 de massa \nNormalmente encontrado no estado líquido; Curiosidade: vapores de Bromo têm a cor avermelhada, e é prejudicial à saúde",
            'Kr': "Criptônio; 36; 83.798 de massa \nNormalmente encontrado no estado gasoso; Curiosidade: aplicado em lâmpadas incandescentes para maior eficiência",
            'Rb': "Rubídio; 37; 85.468 de massa \nNormalmente encontrado no estado sólido; Curiosidade: pode queimar espontaneamente em contato com o ar",
            'Sr': "Estrôncio; 38; 87.62 de massa\nNormalmente encontrado no estado sólido; Curiosidade: um remédio extremamente indicado para quem tem osteoporose",
            'Y': "Ítrio; 39; 88.906 de massa \nNormalmente encontrado no estado sólido; Curiosidade: utilizado em supercondutores",
            'Zr': "Zircônio; 40; 91.224 de massa \nNormalmente encontrado no estado sólido; Curiosidade: pode ser utilizado em implantes dentários",
            'Nb': "Nióbio; 41; 92.90638 de massa \nNormalmente encontrado no estado sólido; Curiosidade: o Brasil possui 90% das reservas desse elemento", 
            'Mo': "Molibdênio; 42; 95.94 de massa \nNormalmente encontrado no estado sólido; Curiosidade: nutriente que garante maior desenvolvimento saúdavel na cultura agrícola",
            'Tc': "Tecnécio; 43; [98] de massa \nNormalmente encontrado no estado sólido; Curiosidade: o primeiro elemento a ser feito artificialmente",
            'Ru': "Rutênio; 44; 101.07 de massa \nNormalmente encontrado no estado sólido: Curiosidade: utilizado no endurecimento de platina e paládio",
            'Rh': "Ródio; 45; 102.90550 de massa \nNormalmente encontrado no estado sólido; Curiosidade: pode ser encontrado em combustível nuclear queimado",
            'Pd': "Paládio; 46; 106.42 de massa \nNormalmente encontrado no estado sólido: Curiosidade: utilizado em equipamento militar, civil e aeroespacial",
            'Ag': "Prata; 47; 107.868 de massa \nNormalmente encontrado no estado sólido; Curiosidade: ainda utilizado em soldas",
            'Cd': "Cádmio; 48; 112.441 de massa \nNormalmente encontrado no estado sólido; Curiosidade: utilizado como anticorrosivo em aço galvanizado",
            'In': "Índio; 49; 114.818 de massa \nNormalmente encontrado no estado sólido; Curiosidade: utilizado na tela de cristais líquidos", 
            'Sn': "Estanho; 50; 118.71 de massa \nNormalmente encontrado no estado sólido; Curiosidade: a primeira descoberta sobre esse elemento foi no Brasil",
            'Cs': "Césio; 55; 132.905 de massa \nNormalmente encontrado no estado líquido/sólido depende da temperatura ambiente; Curiosidade: ocorreu um acidente no Brasil conhecido com césio 137",
            'Ba': "Bário; 56; 137.327 de massa \nNormalmente encontrado no estado sólido; Curiosidade: mais utlizado em remoção de oxigênio em válvulas eletrônicas",
            'La': "Lantânio; 57; 138.905 de massa \nNormalmente encontrado no estado sólido; Curiosidade: utilizado em isqueiros",
            'Ce': "Cério; 58; 140.116 de massa \nNormalmente encontrado no estado sólido; Curiosidade: bastante utilizado em vidraçarias para vários usos",
            'Pr': "Praseodímio; 59; 140.908 de massa \nNormalmente encontrado no estado sólido; Curiosidade: utilizado em lâmpadas de arco de carbono na indústria cinematográfica",
            'Nd': "Neodímio; 60; 144.242 de massa \nNormalmente encontrado no estado sólido; Curiosidade: utilizado para produzir imãs que fazer os motores elétricos girarem",
            'Pm': "Promécio; 61; [145] de massa \nNormalmente encontrado no estado sólido; Curiosidade: utlizado como fonte de energia de decaimento beta",
            'Sm': "Samário; 62; 150.36 de massa \nNormalmente encontrado no estado sólido; Curiosidade: utlizado na produção de imãs permanentes",
            'Eu': "Európio; 63; 151.964 de massa \nNormalmente encontrado no estado sólido; Curiosidade: utlizado em fabricação de telas de tablets, celulares, computadores e telas solares",
            'Gd': "Gadolínio; 64; 157.25 de massa \nNormalmente encontrado no estado sólido; Curiosidade: possui uma propriedade única chamada magnetocalória, que basicamente muda de de temperatura de acordo com o campo magnetico",
            'Tb': "Térbio; 65; 158.925 de massa \nNormalmente encontrado no estado sólido; Curiosidade: utilizado como uma agenete de impurezas em dispositivos seicondutores",
            'Dy': "Disprósio; 66; 162.5 de massa \nNormalmente encontrado no estado sólido; Curiosidade: utilizado para construir materiais laser",
            'Ho': "Hólmio; 67; 164.93032 de massa \nNormalmente encontrado no estado sólido; Curiosidade: utlizado na fabricação de vidros especiais e cerâmicas",
            'Er': "Érbio; 68; 167.259 de massa \nNormalmente encontrado no estado sólido; Curiosidade: geralmente usado com filtro fotográfico",
            'Tm': "Túlio; 69; 168.934 de massa \nNormalmente encontrado no estado sólido; Curiosidade: utlizado em ligas para tecnologia nuclear por conta de ser um absorvente de neutrões",
            'Yb': "Itérbio; 70; 173.04 de massa \nNormalmente encontrado no estado sólido; Curiosidade: utlizado na produção de aços",
            'Lu': "Lutécio; 71; 174.967 de massa \nNormalmente encontrado no estado sólido; Curiosidade: catalisador no craqueamento de petróleo nas refinarias",
            'Hf': "Háfnio; 72; 178.49 de massa \nNormalmente encontrado no estado sólido; Curiosidade: é utilizado como um controlador de nêutrons em geradores nucleares",
            'Ta': "Tântalo; 73; 180.948 de massa \nNormalmente encontrado no estado sólido; Curiosidade: utlizado em baterias de celular",
            'W': "Tungstênio; 74; 183.84 de massa \nNormalmente encontrado no estado sólido; Curiosidade: presente em canetas esferográficas",
            'Re': "Rênio; 75; 186.207 de massa \nNormalmente encontrado no estado líquido; Curiosidade: segundo metal com maior ponto de fusão da tabela periódica",
            'Os': "Ósmio; 76; 190.23 de massa \nNormalmente encontrado no estado sólido; Curiosidade: o nome vem do grego 'osme' que significa cheiro",
            'Ir': "Irídio; 77; 192.217 de massa \nNormalmente encontrado no estado sólido; Curiosidade: o metal mais resistente a corrosão",
            'Pt': "Platina; 78; 195.084 de massa \nNormalmente encontrado no estado sólido; Curiosidade: utilizado em equipamento no laboratório e equipamenteos odontológicos",
            'Au': "Ouro; 79; 196.967 de massa \nNormalmente encontrado no estado sólido; Curiosidade: destaca-se por sua condutividade elevada",
            'Hg': "Mercúrio; 80; 200.59 de massa \nNormalmente encontrado no estado líquido; Curiosidade: um dos primeiros metais a ser manipulado pela humanidade",
            'Tl': "Tálio; 81; 204.383 de massa \nNormalmente encontrado no estado sólido; Curiosaidade: um radiofármaco utilizado na avaliação pré-operatoria de tumores cerebrais",
            'Pb': "Chumbo; 82; 207.2 de massa \nNormalmente encontrado no estado sólido; Curiosidade: um grande problema de bioacumulação na atualidade",
            'Bi': "Bismuto; 83; 208.98 de massa \nNormalmente encontrado no estado sólido; Curiosidade: um dos poucos materiais que se expandem ao se solidificar iqual a água",
            'Po': "Polônio; 84; [210] de massa \nNormalmente encontrado no estado sólido; Curiosidade: um materia descoberto por Marie Curie",
            'At': "Ástato; 85; [210] de massa \nNormalmente encontrado no estado sólido; Curiosidade: entre os halogênios ele é o mais pesado e o mais oxidante",
            'Rn': "Radônio; 86; [220] de massa \nNormalmente encontrado no estado gasoso; Curiosidade: utilizado como fonte de radiação em terapias contra o câncer",
            'Fr': "Frâncio; 87; [223] de massa \nNormalmente encontrado no estado sólido; Curiosidade: utilizado apenas em tarefas de investigação",
            'Ra': "Rádio; 88; [226] de massa \nNormalmente encontrado no estado sólido; Curiosidade: recebeu esse nome por conta do som que ele emitia",
            'Ac': "Actínio; 89; [227] de massa \nNormalmente encontrado no estado sólido; Curiosidade: a partir desse todos da mesma familia são radioativos",
            'Th': "Tório; 90; 232.03806 de massa \nNormalmente encontrado no estado sólido; Curiosidade: utilizado para aumentar a resistencia ao fogo e ao calor",
            'Pa': "Protactínio; 91; 231.03588 de massa \nNormalmente encontrado no estado sólido; Curiosidade: tem o tempo de meia-vida de 1,17 minutos",
            'U': "Urânio; 92; 238.02891 de massa \nNormalmente encontrado no estado sólido; Curiosidade: quase todo Brasil utiliza-o como produção de energia",
            'Np': "Neptúnio; 93; [237] de massa \nNormalmente encontrado no estado sólido; Curiosidade: tem o tempo de meia-vida de 2,1 dias",
            'Pu': "Plutônio; 94; [224] de massa \nNormalmente encontrado no estado sólido; Curiosidade: este elemento contém diversos isótopos",
            'Am': "Amerício; 95; [243] de massa \nNormalmente encontrado no estado sólido; Curiosidade: utilizado em detectores de fumaça",
            'Cm': "Cúrio; 96; [247] de massa \nNormalmente encontrado no estado sólido; Curiosidade: utilizado em marcapassos",
            'Bk': "Berquélio; 97; [247] de massa \nNormalmente encontrado no estado sólido; Curiosidade: o isotopo mais estável tem o tempo de meia-vida de 1380 anos",
            'Cf': "Califório; 98; [251] de massa \nNormalmente encontrado no estado sólido; Curiosidade: o isotopo mais estável tem o tempo de meia-vida de 700 anos",
            'Es': "Einténio; 99; [252] de massa \nNormalmente encontrado no estado sólido; Curiosidade: decai por emissão alfa",
            'Fm': "Férmio; 100; [257] de massa \nNormalmente encontrado no estado sólido; Curiosidade: ele não possui aplicação em nenhuma área",
            'Md': "Mendelévio; 101; [258] de massa \nNormalmente encontrado no estado sólido; Curiosidade: ele não possui aplicação em nenhuma área",
            'No': "Nobélio; 102; [259] de massa \nNormalmente encontrado no estado sólido; Curiosidade: ele nao possui aplicação em nenhuma área",
            'Lr': "Laurêncio; 103; [262] de massa \nNormalmente encontrado no estado sólido; Curiosidade: ele nao possui aplicação em nenhuma área",
            'Rf': "Rutherfórdio; 104; 261 de massa \nNormalmente encontrado no estado sólido; Curiosidade: ele nao possui aplicação em nenhuma área",
            'Db': "Dúbnio; 105; [262] de massa \nNormalmente encontrado no estado sólido; Curiosidade: ele nao possui aplicação em nenhuma área",
            'Sg': "Seabórgio; 106; [266] de massa \nNormalmente encontrado no estado sólido; Curiosidade: ele nao possui aplicação em nenhuma área",
            'Bh': "Bóhrio; 107; [264] de massa \nNormalmente encontrado no estado sólido; Curiosidade: ele nao possui aplicação em nenhuma área",
            'Hs': "Hássio; 108; [227] de massa \nNormalmente encontrado no estado sólido; Curiosidade: ele nao possui aplicação em nenhuma área",
            'Mt': "Meitnério; 109; [268] de massa \nNormalmente encontrado no estado sólido; Curiosidade: ele nao possui aplicação em nenhuma área",
            'Ds': "Darmstádio; 110; [271] de massa \nNormalmente encontrado no estado sólido; Curiosidade: ele nao possui aplicação em nenhuma área",
            'Rg':  "Roentgênio; 111; [272] de massa \nNormalmente encontrado no estado sólido; Curiosidade: ele nao possui aplicação em nenhuma área",
            'Cn': "Copernício; 112; [277] de massa \nNormalmente encontrado no estado sólido; Curiosidade: ele nao possui aplicação em nenhuma área",
            'Nh': "Nihônio; 113; [286] de massa \nNormalmente encontrado no estado sólido; Curiosidade: ele nao possui aplicação em nenhuma área",
            'Fl': "Fleróvio; 114; [289] de massa \nNormalmente encontrado no estado sólido; Curiosidade: ele nao possui aplicação em nenhuma área",
            'Mc': "Moscóvio; 115; [288] de massa \nNormalmente encontrado no estado sólido; Curiosidade: ele nao possui aplicação em nenhuma área",
            'Lv': "Livermório; 116; [293] de massa \nNormalmente encontrado no estado sólido; Curiosidade: ele nao possui aplicação em nenhuma área",
            'Ts': "Tenessino; 117; [294] de massa \nNormalmente encontrado no estado sólido; Curiosidade: ele nao possui aplicação em nenhuma área",
            'Og': "Oganessônio; 118; [294] de massa\nNormalmente encontrado no estado sólido; Curiosidade: ele nao possui aplicação em nenhuma área",
        }
def buscar_elemento():
    simbolo = entrada.get().strip().capitalize()
    if simbolo.lower() == "sair":
        encerrar_programa()
        return
    
    info = elements.get(simbolo)
    if info:
        resultado_texto.config(state=tk.NORMAL)
        resultado_texto.delete("1.0", tk.END)
        resultado_texto.insert(tk.END, f"{info}")
        resultado_texto.config(state=tk.DISABLED)
    else:
        messagebox.showerror("Erro", "Elemento não identificado.\nDigite um símbolo válido (ex: H, O, Na, Fe...)")

# Função para encerrar o programa (chamada ao apertar 'X' ou digitar "Sair")
def encerrar_programa():
    if messagebox.askyesno("Encerrar", "Tem certeza que deseja sair?"):
        janela.destroy()  # Fecha a janela e encerra o programa

# Interface principal
janela = tk.Tk()
janela.title("Tabela Periódica Interativa")
janela.geometry("700x400")
janela.config(bg="#e0ffe0")

# Intercepta o clique no botão X
janela.protocol("WM_DELETE_WINDOW", encerrar_programa)

# Título
titulo = tk.Label(
    janela, 
    text="🔬 Tabela Periódica Interativa", 
    font=("Arial", 16, "bold"), 
    bg="#e0ffe0", 
    fg="#004400"
)
titulo.pack(pady=10)

# Campo de entrada
frame_entrada = tk.Frame(janela, bg="#e0ffe0")
frame_entrada.pack(pady=10)

tk.Label(frame_entrada, text="Digite o símbolo do elemento:", bg="#e0ffe0", font=("Arial", 12)).pack(side=tk.LEFT)
entrada = tk.Entry(frame_entrada, width=10, font=("Arial", 12))
entrada.pack(side=tk.LEFT, padx=5)

botao_buscar = tk.Button(frame_entrada, text="Buscar", command=buscar_elemento, font=("Arial", 12), bg="#90ee90")
botao_buscar.pack(side=tk.LEFT, padx=5)

# Área de resultado
resultado_frame = tk.Frame(janela, bg="#e0ffe0")
resultado_frame.pack(pady=20)

resultado_texto = tk.Text(resultado_frame, width=80, height=10, wrap="word", font=("Arial", 11))
resultado_texto.pack()
resultado_texto.config(state=tk.DISABLED)

# Rodapé
rodape = tk.Label(
    janela, 
    text="Digite 'Sair' ou clique no X para encerrar o programa", 
    font=("Arial", 10, "italic"), 
    bg="#e0ffe0", 
    fg="#555"
)
rodape.pack(pady=10)

# Loop principal
janela.mainloop()