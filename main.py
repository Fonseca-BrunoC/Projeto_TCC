from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import os
import shutil
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import pandas as pd
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRoundFlatButton
from importlib import reload
import webbrowser as wb


class LoadDialog(MDBoxLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    card = ObjectProperty(None)

class ResultDialog1(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.p = Monod_MP1().model()
        mimax = str(round(self.p[0], 5))
        ks = str(round(self.p[1], 5))
        yxs = str(round(self.p[2], 5))
        kd = str(round(self.p[3], 5))
        alfa = str(round(self.p[4], 5))
        Table = MDDataTable(size_hint= (1, 0.3),
                            pos_hint= {'center_x':0.8, 'center_y':0.8},
                            column_data= [("Mimax", dp(28)), ("Ks", dp(28)), ("Yxs", dp(28)),
                                          ("Kd", dp(28)), ("Alfa", dp(28)),],
                            row_data= [(f"{mimax}", f"{ks}", f"{yxs}", f"{kd}", f"{alfa}"),
                                       ("", "", "", "", "")])
        tabela = self.ids.tabela1
        tabela.add_widget(Table)

    def m_grafico(self):
        self.g = Monod_MP1().modelgraph()
        return self.g

    def m_prod_grafico(self):
        self.g1 = Monod_MP1().model_prod_graph()
        return self.g1

    def m_mi_grafico(self):
        self.g2 = Monod_MP1().model_mi_graph()
        return self.g2

    cancel2 = ObjectProperty(None)

class ResultDialog2(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.p = Monod_MP2().model()
        mimax = str(round(self.p[0], 5))
        ks = str(round(self.p[1], 5))
        yxs = str(round(self.p[2], 5))
        kd = str(round(self.p[3], 5))
        beta = str(round(self.p[4], 5))
        Table = MDDataTable(size_hint= (1, 0.3),
                            pos_hint= {'center_x':0.8, 'center_y':0.8},
                            column_data= [("Mimax", dp(28)), ("Ks", dp(28)), ("Yxs", dp(28)),
                                          ("Kd", dp(28)), ("Beta", dp(28)),],
                            row_data= [(f"{mimax}", f"{ks}", f"{yxs}", f"{kd}", f"{beta}"),
                                       ("", "", "", "", "")])
        tabela = self.ids.tabela2
        tabela.add_widget(Table)

    def m_grafico(self):
        self.g = Monod_MP2().modelgraph()
        return self.g

    def m_prod_grafico(self):
        self.g1 = Monod_MP2().model_prod_graph()
        return self.g1

    def m_mi_grafico(self):
        self.g2 = Monod_MP2().model_mi_graph()
        return self.g2

    cancel3 = ObjectProperty(None)

class ResultDialog3(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.p = Monod_MP3().model()
        mimax = str(round(self.p[0], 5))
        ks = str(round(self.p[1], 5))
        yxs = str(round(self.p[2], 5))
        kd = str(round(self.p[3], 5))
        alfa = str(round(self.p[4], 5))
        beta = str(round(self.p[5], 5))
        Table = MDDataTable(size_hint= (1, 0.3),
                            pos_hint= {'center_x':0.8, 'center_y':0.8},
                            column_data= [("Mimax", dp(22)), ("Ks", dp(22)), ("Yxs", dp(22)),
                                          ("Kd", dp(22)), ("Alfa", dp(22)), ("Beta", dp(22))],
                            row_data= [(f"{mimax}", f"{ks}", f"{yxs}", f"{kd}", f"{alfa}", f"{beta}"),
                                       ("", "", "", "", "", "")])
        tabela = self.ids.tabela3
        tabela.add_widget(Table)

    def m_grafico(self):
        self.g = Monod_MP3().modelgraph()
        return self.g

    def m_prod_grafico(self):
        self.g1 = Monod_MP3().model_prod_graph()
        return self.g1

    def m_mi_grafico(self):
        self.g2 = Monod_MP3().model_mi_graph()
        return self.g2


    cancel4 = ObjectProperty(None)


class ResultDialog_Mod_Andrews1(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.p = Andrews_MP1().model()
        mimax = str(round(self.p[0], 5))
        ks = str(round(self.p[1], 5))
        ki = str(round(self.p[2], 5))
        yxs = str(round(self.p[3], 5))
        kd = str(round(self.p[4], 5))
        alfa = str(round(self.p[5], 5))
        Table = MDDataTable(size_hint= (1, 0.3),
                            pos_hint= {'center_x':0.8, 'center_y':0.8},
                            column_data= [("Mimax", dp(22)), ("Ks", dp(22)), ("Ki", dp(22)), ("Yxs", dp(22)),
                                          ("Kd", dp(22)), ("Alfa", dp(22)),],
                            row_data= [(f"{mimax}", f"{ks}", f"{ki}", f"{yxs}", f"{kd}", f"{alfa}"),
                                       ("", "", "", "", "", "")])
        tabela = self.ids.tabela1
        tabela.add_widget(Table)

    def m_grafico(self):
        self.g = Andrews_MP1().modelgraph()
        return self.g

    def m_prod_grafico(self):
        self.g1 = Andrews_MP1().model_prod_graph()
        return self.g1

    def m_mi_grafico(self):
        self.g2 = Andrews_MP1().model_mi_graph()
        return self.g2

    cancel2 = ObjectProperty(None)

class ResultDialog_Mod_Andrews2(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.p = Andrews_MP2().model()
        mimax = str(round(self.p[0], 5))
        ks = str(round(self.p[1], 5))
        ki = str(round(self.p[2], 5))
        yxs = str(round(self.p[3], 5))
        kd = str(round(self.p[4], 5))
        beta = str(round(self.p[5], 5))
        Table = MDDataTable(size_hint= (1, 0.3),
                            pos_hint= {'center_x':0.8, 'center_y':0.8},
                            column_data= [("Mimax", dp(22)), ("Ks", dp(22)), ("Ki", dp(22)), ("Yxs", dp(22)),
                                          ("Kd", dp(22)), ("Beta", dp(22))],
                            row_data= [(f"{mimax}", f"{ks}", f"{ki}", f"{yxs}", f"{kd}", f"{beta}"),
                                       ("", "", "", "", "", "")])
        tabela = self.ids.tabela1
        tabela.add_widget(Table)

    def m_grafico(self):
        self.g = Andrews_MP2().modelgraph()
        return self.g

    def m_prod_grafico(self):
        self.g1 = Andrews_MP2().model_prod_graph()
        return self.g1

    def m_mi_grafico(self):
        self.g2 = Andrews_MP2().model_mi_graph()
        return self.g2

    cancel2 = ObjectProperty(None)

class ResultDialog_Mod_Andrews3(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.p = Andrews_MP3().model()
        mimax = str(round(self.p[0], 5))
        ks = str(round(self.p[1], 5))
        ki = str(round(self.p[2], 5))
        yxs = str(round(self.p[3], 5))
        kd = str(round(self.p[4], 5))
        alfa = str(round(self.p[5], 5))
        beta = str(round(self.p[6], 5))
        Table = MDDataTable(size_hint= (1, 0.3),
                            pos_hint= {'center_x':0.8, 'center_y':0.8},
                            column_data= [("Mimax", dp(28)), ("Ks", dp(28)), ("Ki", dp(28)), ("Yxs", dp(28)),
                                          ("Kd", dp(28)), ("Alfa", dp(28)), ("Beta", dp(28)),],
                            row_data= [(f"{mimax}", f"{ks}", f"{ki}", f"{yxs}", f"{kd}", f"{alfa}", f"{beta}"),
                                       ("", "", "", "", "", "", "")])
        tabela = self.ids.tabela1 #lembrar de mudar
        tabela.add_widget(Table)

    def m_grafico(self):
        self.g = Andrews_MP3().modelgraph()
        return self.g

    def m_prod_grafico(self):
        self.g1 = Andrews_MP3().model_prod_graph()
        return self.g1

    def m_mi_grafico(self):
        self.g2 = Andrews_MP3().model_mi_graph()
        return self.g2

    cancel2 = ObjectProperty(None)


class ResultDialog_Mod_Aiba1(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.p = Aiba_Shoda_Nagatani_MP1().model()
        mimax = str(round(self.p[0], 5))
        ks = str(round(self.p[1], 5))
        ki = str(round(self.p[2], 5))
        yxs = str(round(self.p[3], 5))
        kd = str(round(self.p[4], 5))
        alfa = str(round(self.p[5], 5))
        Table = MDDataTable(size_hint= (1, 0.3),
                            pos_hint= {'center_x':0.8, 'center_y':0.8},
                            column_data= [("Mimax", dp(22)), ("Ks", dp(22)), ("Ki", dp(22)), ("Yxs", dp(22)),
                                          ("Kd", dp(22)), ("Alfa", dp(22)),],
                            row_data= [(f"{mimax}", f"{ks}", f"{ki}", f"{yxs}", f"{kd}", f"{alfa}"),
                                       ("", "", "", "", "", "")])
        tabela = self.ids.tabela1
        tabela.add_widget(Table)

    def m_grafico(self):
        self.g = Aiba_Shoda_Nagatani_MP1().modelgraph()
        return self.g

    def m_prod_grafico(self):
        self.g1 = Aiba_Shoda_Nagatani_MP1().model_prod_graph()
        return self.g1

    def m_mi_grafico(self):
        self.g2 = Aiba_Shoda_Nagatani_MP1().model_mi_graph()
        return self.g2

    cancel2 = ObjectProperty(None)


class ResultDialog_Mod_Aiba2(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.p = Aiba_Shoda_Nagatani_MP2().model()
        mimax = str(round(self.p[0], 5))
        ks = str(round(self.p[1], 5))
        ki = str(round(self.p[2], 5))
        yxs = str(round(self.p[3], 5))
        kd = str(round(self.p[4], 5))
        beta = str(round(self.p[5], 5))
        Table = MDDataTable(size_hint= (1, 0.3),
                            pos_hint= {'center_x':0.8, 'center_y':0.8},
                            column_data= [("Mimax", dp(22)), ("Ks", dp(22)), ("Ki", dp(22)), ("Yxs", dp(22)),
                                          ("Kd", dp(22)), ("Beta", dp(22))],
                            row_data= [(f"{mimax}", f"{ks}", f"{ki}", f"{yxs}", f"{kd}", f"{beta}"),
                                       ("", "", "", "", "", "")])
        tabela = self.ids.tabela1
        tabela.add_widget(Table)

    def m_grafico(self):
        self.g = Aiba_Shoda_Nagatani_MP2().modelgraph()
        return self.g

    def m_prod_grafico(self):
        self.g1 = Aiba_Shoda_Nagatani_MP2().model_prod_graph()
        return self.g1

    def m_mi_grafico(self):
        self.g2 = Aiba_Shoda_Nagatani_MP2().model_mi_graph()
        return self.g2

    cancel2 = ObjectProperty(None)

class ResultDialog_Mod_Aiba3(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.p = Aiba_Shoda_Nagatani_MP3().model()
        mimax = str(round(self.p[0], 5))
        ks = str(round(self.p[1], 5))
        ki = str(round(self.p[2], 5))
        yxs = str(round(self.p[3], 5))
        kd = str(round(self.p[4], 5))
        alfa = str(round(self.p[5], 5))
        beta = str(round(self.p[6], 5))
        Table = MDDataTable(size_hint= (1, 0.3),
                            pos_hint= {'center_x':0.8, 'center_y':0.8},
                            column_data= [("Mimax", dp(28)), ("Ks", dp(28)), ("Ki", dp(28)), ("Yxs", dp(28)),
                                          ("Kd", dp(28)), ("Alfa", dp(28)), ("Beta", dp(28)),],
                            row_data= [(f"{mimax}", f"{ks}", f"{ki}", f"{yxs}", f"{kd}", f"{alfa}", f"{beta}"),
                                       ("", "", "", "", "", "", "")])
        tabela = self.ids.tabela1 #lembrar de mudar
        tabela.add_widget(Table)

    def m_grafico(self):
        self.g = Aiba_Shoda_Nagatani_MP3().modelgraph()
        return self.g

    def m_prod_grafico(self):
        self.g1 = Aiba_Shoda_Nagatani_MP3().model_prod_graph()
        return self.g1

    def m_mi_grafico(self):
        self.g2 = Aiba_Shoda_Nagatani_MP3().model_mi_graph()
        return self.g2

    cancel2 = ObjectProperty(None)

class ResultDialog_Sim1(FloatLayout):
    def sim_grafico(self):
        self.g1 = Monod_SP1().simu_graph()
        return self.g1

    def sim_prod_grafico(self):
        self.g1 = Monod_SP1().simu_prod_graph()
        return self.g1

    def sim_mi_grafico(self):
        self.g2 = Monod_SP1().simu_mi_graph()
        return self.g2

    def save(self):
        self.dados = Monod_SP1().dados()
        return self.dados

    def save_dialog(self):
        self.dir = os.getcwd()
        close_button = MDFlatButton(text = 'Fechar', on_release=self.close_dialog)
        self.dialog = MDDialog(title = 'O arquivo foi salvo no formato .xlsx no diretório:', text = self.dir,
                               size_hint=(0.5, 1),
                               buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    cancel5 = ObjectProperty(None)


class ResultDialog_Sim2(FloatLayout):
    def sim_grafico(self):
        self.g = Monod_SP2().simu_graph()
        return self.g

    def sim_prod_grafico(self):
        self.g1 = Monod_SP2().simu_prod_graph()
        return self.g1

    def sim_mi_grafico(self):
        self.g2 = Monod_SP2().simu_mi_graph()
        return self.g2

    def save(self):
        self.dados = Monod_SP2().dados()
        return self.dados

    def save_dialog(self):
        self.dir = os.getcwd()
        close_button = MDFlatButton(text = 'Fechar', on_release=self.close_dialog)
        self.dialog = MDDialog(title = 'O arquivo foi salvo no formato .xlsx no diretório:', text = self.dir,
                               size_hint=(0.5, 1),
                               buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    cancel6 = ObjectProperty(None)


class ResultDialog_Sim3(FloatLayout):
    def sim_grafico(self):
        self.g = Monod_SP3().simu_graph()
        return self.g

    def sim_prod_grafico(self):
        self.g1 = Monod_SP3().simu_prod_graph()
        return self.g1

    def sim_mi_grafico(self):
        self.g2 = Monod_SP3().simu_mi_graph()
        return self.g2

    def save(self):
        self.dados = Monod_SP3().dados()
        return self.dados

    def save_dialog(self):
        self.dir = os.getcwd()
        close_button = MDFlatButton(text = 'Fechar', on_release=self.close_dialog)
        self.dialog = MDDialog(title = 'O arquivo foi salvo no formato .xlsx no diretório:', text = self.dir,
                               size_hint=(0.5, 1),
                               buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    cancel7 = ObjectProperty(None)


class ResultDialog_Andrews_Sim1(FloatLayout):
    def sim_grafico(self):
        self.g1 = Andrews_SP1().simu_graph()
        return self.g1

    def sim_prod_grafico(self):
        self.g1 = Andrews_SP1().simu_prod_graph()
        return self.g1

    def sim_mi_grafico(self):
        self.g2 = Andrews_SP1().simu_mi_graph()
        return self.g2

    def save(self):
        self.dados = Andrews_SP1().dados()
        return self.dados

    def save_dialog(self):
        self.dir = os.getcwd()
        close_button = MDFlatButton(text = 'Fechar', on_release=self.close_dialog)
        self.dialog = MDDialog(title = 'O arquivo foi salvo no formato .xlsx no diretório:', text = self.dir,
                               size_hint=(0.5, 1),
                               buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    cancel5 = ObjectProperty(None)


class ResultDialog_Andrews_Sim2(FloatLayout):
    def sim_grafico(self):
        self.g = Andrews_SP2().simu_graph()
        return self.g

    def sim_prod_grafico(self):
        self.g1 = Andrews_SP2().simu_prod_graph()
        return self.g1

    def sim_mi_grafico(self):
        self.g2 = Andrews_SP2().simu_mi_graph()
        return self.g2

    def save(self):
        self.dados = Andrews_SP2().dados()
        return self.dados

    def save_dialog(self):
        self.dir = os.getcwd()
        close_button = MDFlatButton(text = 'Fechar', on_release=self.close_dialog)
        self.dialog = MDDialog(title = 'O arquivo foi salvo no formato .xlsx no diretório:', text = self.dir,
                               size_hint=(0.5, 1),
                               buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    cancel6 = ObjectProperty(None)


class ResultDialog_Andrews_Sim3(FloatLayout):
    def sim_grafico(self):
        self.g = Andrews_SP3().simu_graph()
        return self.g

    def sim_prod_grafico(self):
        self.g1 = Andrews_SP3().simu_prod_graph()
        return self.g1

    def sim_mi_grafico(self):
        self.g2 = Andrews_SP3().simu_mi_graph()
        return self.g2

    def save(self):
        self.dados = Andrews_SP3().dados()
        return self.dados

    def save_dialog(self):
        self.dir = os.getcwd()
        close_button = MDFlatButton(text = 'Fechar', on_release=self.close_dialog)
        self.dialog = MDDialog(title = 'O arquivo foi salvo no formato .xlsx no diretório:', text = self.dir,
                               size_hint=(0.5, 1),
                               buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    cancel7 = ObjectProperty(None)

class ResultDialog_Aiba_Sim1(FloatLayout):
    def sim_grafico(self):
        self.g1 = Aiba_Shoda_Nagatani_SP1().simu_graph()
        return self.g1

    def sim_prod_grafico(self):
        self.g1 = Aiba_Shoda_Nagatani_SP1().simu_prod_graph()
        return self.g1

    def sim_mi_grafico(self):
        self.g2 = Aiba_Shoda_Nagatani_SP1().simu_mi_graph()
        return self.g2

    def save(self):
        self.dados = Aiba_Shoda_Nagatani_SP1().dados()
        return self.dados

    def save_dialog(self):
        self.dir = os.getcwd()
        close_button = MDFlatButton(text = 'Fechar', on_release=self.close_dialog)
        self.dialog = MDDialog(title = 'O arquivo foi salvo no formato .xlsx no diretório:', text = self.dir,
                               size_hint=(0.5, 1),
                               buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    cancel5 = ObjectProperty(None)

class ResultDialog_Aiba_Sim2(FloatLayout):
    def sim_grafico(self):
        self.g = Aiba_Shoda_Nagatani_SP2().simu_graph()
        return self.g

    def sim_prod_grafico(self):
        self.g1 = Aiba_Shoda_Nagatani_SP2().simu_prod_graph()
        return self.g1

    def sim_mi_grafico(self):
        self.g2 = Aiba_Shoda_Nagatani_SP2().simu_mi_graph()
        return self.g2

    def save(self):
        self.dados = Aiba_Shoda_Nagatani_SP2().dados()
        return self.dados

    def save_dialog(self):
        self.dir = os.getcwd()
        close_button = MDFlatButton(text = 'Fechar', on_release=self.close_dialog)
        self.dialog = MDDialog(title = 'O arquivo foi salvo no formato .xlsx no diretório:', text = self.dir,
                               size_hint=(0.5, 1),
                               buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    cancel6 = ObjectProperty(None)

class ResultDialog_Aiba_Sim3(FloatLayout):
    def sim_grafico(self):
        self.g = Aiba_Shoda_Nagatani_SP3().simu_graph()
        return self.g

    def sim_prod_grafico(self):
        self.g1 = Aiba_Shoda_Nagatani_SP3().simu_prod_graph()
        return self.g1

    def sim_mi_grafico(self):
        self.g2 = Aiba_Shoda_Nagatani_SP3().simu_mi_graph()
        return self.g2

    def save(self):
        self.dados = Aiba_Shoda_Nagatani_SP3().dados()
        return self.dados

    def save_dialog(self):
        self.dir = os.getcwd()
        close_button = MDFlatButton(text = 'Fechar', on_release=self.close_dialog)
        self.dialog = MDDialog(title = 'O arquivo foi salvo no formato .xlsx no diretório:', text = self.dir,
                               size_hint=(0.5, 1),
                               buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    cancel7 = ObjectProperty(None)


class Home(Screen):
    def documentacao(self):
        return wb.open("https://fonseca-brunoc.github.io")

class Modelagem(Screen):
    pass

class Escolha_M1(Screen):
    pass

class Monod_MP1(Screen):
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content_1 = LoadDialog(load=self.load, cancel=self.card)
        self._popup = Popup(title="Load file", content=content_1,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        arq_txt = open("caminho.txt", "a")
        arq_txt.write(f'{os.path.join(path, filename[0])}')

        cwd = os.getcwd()

        path_splited = path.split()
        filename2 = ''
        for i in path_splited:
            filename2 = filename[0].replace(i, '')

        caminho = f'{os.path.join(path, filename[0])}'
        destino = cwd

        shutil.copy2(caminho, destino)
        filename2 = destino + filename2
        file_newname_newfile = os.path.join(destino, 'Dados.xlsx')
        shutil.move(filename2, file_newname_newfile)

    def card(self):
        local = os.getcwd()

        if os.path.isfile(local + '/caminho.txt'):
            nome = open("caminho.txt", "r")
            nome = nome.read()
            nome = str(nome)

            iniciar_button = MDRoundFlatButton(text= 'Iniciar modelagem', on_release = self.show_result)
            close_button = MDFlatButton(text = 'Cancelar', on_release = self.close_dialog)
            self.dialog = MDDialog(text = f'{nome}',
                               size_hint=(0.5, 1),
                               buttons=[iniciar_button, close_button])
            self.dialog.open()
        self._popup.dismiss()

    def show_result(self, obj):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            content_1_2 = ResultDialog1(cancel2=self.dismiss_popup)
            self._popup = Popup(title="Resultados", content=content_1_2,
                                size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
            self._popup.open()
            self.limpar_caminho()

        else:
            pass

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def model(self):
        import modelagem
        return modelagem.result1()

    def modelgraph(self):
        import modelagem
        return modelagem.plot1()

    def model_prod_graph(self):
        import modelagem
        return modelagem.grafico_produtividade1()

    def model_mi_graph(self):
        import modelagem
        return modelagem.grafico_mi1()

    def reload_f(self):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            import modelagem
            return reload(modelagem)
        else: pass

    def limpar_arquivo(self):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            return os.remove('Dados.xlsx')
        else: pass

    def limpar_caminho(self):
        local = os.getcwd()
        if os.path.isfile(local + '/caminho.txt'):
            return os.remove('caminho.txt')
        else: pass

class Moser_MP1(Screen):
    pass

class Tessier_MP1(Screen):
    pass

class Andrews_MP1(Screen):
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content_1 = LoadDialog(load=self.load, cancel=self.card)
        self._popup = Popup(title="Load file", content=content_1,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        arq_txt = open("caminho.txt", "a")
        arq_txt.write(f'{os.path.join(path, filename[0])}')

        cwd = os.getcwd()

        path_splited = path.split()
        filename2 = ''
        for i in path_splited:
            filename2 = filename[0].replace(i, '')

        caminho = f'{os.path.join(path, filename[0])}'
        destino = cwd

        shutil.copy2(caminho, destino)
        filename2 = destino + filename2
        file_newname_newfile = os.path.join(destino, 'Dados.xlsx')
        shutil.move(filename2, file_newname_newfile)

    def card(self):
        local = os.getcwd()

        if os.path.isfile(local + '/caminho.txt'):
            nome = open("caminho.txt", "r")
            nome = nome.read()
            nome = str(nome)

            iniciar_button = MDRoundFlatButton(text= 'Iniciar modelagem', on_release = self.show_result)
            close_button = MDFlatButton(text = 'Cancelar', on_release = self.close_dialog)
            self.dialog = MDDialog(text = f'{nome}',
                               size_hint=(0.5, 1),
                               buttons=[iniciar_button, close_button])
            self.dialog.open()
        self._popup.dismiss()


    def show_result(self, obj):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            content_1_2 = ResultDialog_Mod_Andrews1(cancel2=self.dismiss_popup)
            self._popup = Popup(title="Resultados", content=content_1_2,
                                size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
            self._popup.open()
            self.limpar_caminho()

        else:
            pass

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def model(self):
        import mod_andrews
        return mod_andrews.result1()

    def modelgraph(self):
        import mod_andrews
        return mod_andrews.plot1()

    def model_prod_graph(self):
        import mod_andrews
        return mod_andrews.grafico_produtividade1()

    def model_mi_graph(self):
        import mod_andrews
        return mod_andrews.grafico_mi1()

    def reload_f(self):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            import mod_andrews
            return reload(mod_andrews)
        else: pass

    def limpar_arquivo(self):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            return os.remove('Dados.xlsx')
        else: pass

    def limpar_caminho(self):
        local = os.getcwd()
        if os.path.isfile(local + '/caminho.txt'):
            return os.remove('caminho.txt')
        else: pass

class Levenspiel_MP1(Screen):
    pass

class Aiba_Shoda_Nagatani_MP1(Screen):
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content_1 = LoadDialog(load=self.load, cancel=self.card)
        self._popup = Popup(title="Load file", content=content_1,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        arq_txt = open("caminho.txt", "a")
        arq_txt.write(f'{os.path.join(path, filename[0])}')

        cwd = os.getcwd()

        path_splited = path.split()
        filename2 = ''
        for i in path_splited:
            filename2 = filename[0].replace(i, '')

        caminho = f'{os.path.join(path, filename[0])}'
        destino = cwd

        shutil.copy2(caminho, destino)
        filename2 = destino + filename2
        file_newname_newfile = os.path.join(destino, 'Dados.xlsx')
        shutil.move(filename2, file_newname_newfile)

    def card(self):
        local = os.getcwd()

        if os.path.isfile(local + '/caminho.txt'):
            nome = open("caminho.txt", "r")
            nome = nome.read()
            nome = str(nome)

            iniciar_button = MDRoundFlatButton(text= 'Iniciar modelagem', on_release = self.show_result)
            close_button = MDFlatButton(text = 'Cancelar', on_release = self.close_dialog)
            self.dialog = MDDialog(text = f'{nome}',
                               size_hint=(0.5, 1),
                               buttons=[iniciar_button, close_button])
            self.dialog.open()
        self._popup.dismiss()

    def show_result(self, obj):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            content_1_2 = ResultDialog_Mod_Aiba1(cancel2=self.dismiss_popup)
            self._popup = Popup(title="Resultados", content=content_1_2,
                                size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
            self._popup.open()
            self.limpar_caminho()

        else:
            pass

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def model(self):
        import mod_aiba_shoda
        return mod_aiba_shoda.result1()

    def modelgraph(self):
        import mod_aiba_shoda
        return mod_aiba_shoda.plot1()

    def model_prod_graph(self):
        import mod_aiba_shoda
        return mod_aiba_shoda.grafico_produtividade1()

    def model_mi_graph(self):
        import mod_aiba_shoda
        return mod_aiba_shoda.grafico_mi1()

    def reload_f(self):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            import mod_aiba_shoda
            return reload(mod_aiba_shoda)
        else: pass

    def limpar_arquivo(self):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            return os.remove('Dados.xlsx')
        else: pass

    def limpar_caminho(self):
        local = os.getcwd()
        if os.path.isfile(local + '/caminho.txt'):
            return os.remove('caminho.txt')
        else: pass

class Escolha_M2(Screen):
    pass

class Monod_MP2(Screen):
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content_2 = LoadDialog(load=self.load, cancel=self.card)
        self._popup = Popup(title="Load file", content=content_2,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        arq_txt = open("caminho.txt", "a")
        arq_txt.write(f'{os.path.join(path, filename[0])}')

        cwd = os.getcwd()

        path_splited = path.split()
        filename2 = ''
        for i in path_splited:
            filename2 = filename[0].replace(i, '')

        caminho = f'{os.path.join(path, filename[0])}'
        destino = cwd

        shutil.copy2(caminho, destino)
        filename2 = destino + filename2
        file_newname_newfile = os.path.join(destino, 'Dados.xlsx')
        shutil.move(filename2, file_newname_newfile)

    def card(self):
        local = os.getcwd()

        if os.path.isfile(local + '/caminho.txt'):
            nome = open("caminho.txt", "r")
            nome = nome.read()
            nome = str(nome)

            iniciar_button = MDRoundFlatButton(text= 'Iniciar modelagem', on_release = self.show_result)
            close_button = MDFlatButton(text = 'Cancelar', on_release = self.close_dialog)
            self.dialog = MDDialog(text = f'{nome}',
                               size_hint=(0.5, 1),
                               buttons=[iniciar_button, close_button])
            self.dialog.open()
        self._popup.dismiss()

    def show_result(self, obj):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            content_1_2 = ResultDialog2(cancel3=self.dismiss_popup)
            self._popup = Popup(title="Resultados", content=content_1_2,
                                size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
            self._popup.open()
            self.limpar_caminho()

        else:
            pass

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def model(self):
        import modelagem
        return modelagem.result2()

    def modelgraph(self):
        import modelagem
        return modelagem.plot2()

    def model_prod_graph(self):
        import modelagem
        return modelagem.grafico_produtividade2()

    def model_mi_graph(self):
        import modelagem
        return modelagem.grafico_mi2()

    def reload_f(self):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            import modelagem
            return reload(modelagem)
        else: pass

    def limpar_arquivo(self):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            return os.remove('Dados.xlsx')
        else: pass

    def limpar_caminho(self):
        local = os.getcwd()
        if os.path.isfile(local + '/caminho.txt'):
            return os.remove('caminho.txt')
        else: pass

class Moser_MP2(Screen):
    pass

class Tessier_MP2(Screen):
    pass

class Andrews_MP2(Screen):
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content_1 = LoadDialog(load=self.load, cancel=self.card)
        self._popup = Popup(title="Load file", content=content_1,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        arq_txt = open("caminho.txt", "a")
        arq_txt.write(f'{os.path.join(path, filename[0])}')

        cwd = os.getcwd()

        path_splited = path.split()
        filename2 = ''
        for i in path_splited:
            filename2 = filename[0].replace(i, '')

        caminho = f'{os.path.join(path, filename[0])}'
        destino = cwd

        shutil.copy2(caminho, destino)
        filename2 = destino + filename2
        file_newname_newfile = os.path.join(destino, 'Dados.xlsx')
        shutil.move(filename2, file_newname_newfile)

    def card(self):
        local = os.getcwd()

        if os.path.isfile(local + '/caminho.txt'):
            nome = open("caminho.txt", "r")
            nome = nome.read()
            nome = str(nome)

            iniciar_button = MDRoundFlatButton(text= 'Iniciar modelagem', on_release = self.show_result)
            close_button = MDFlatButton(text = 'Cancelar', on_release = self.close_dialog)
            self.dialog = MDDialog(text = f'{nome}',
                               size_hint=(0.5, 1),
                               buttons=[iniciar_button, close_button])
            self.dialog.open()
        self._popup.dismiss()

    def show_result(self, obj):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            content_1_2 = ResultDialog_Mod_Andrews2(cancel2=self.dismiss_popup)
            self._popup = Popup(title="Resultados", content=content_1_2,
                                size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
            self._popup.open()
            self.limpar_caminho()

        else:
            pass

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def model(self):
        import mod_andrews
        return mod_andrews.result2()

    def modelgraph(self):
        import mod_andrews
        return mod_andrews.plot2()

    def model_prod_graph(self):
        import mod_andrews
        return mod_andrews.grafico_produtividade2()

    def model_mi_graph(self):
        import mod_andrews
        return mod_andrews.grafico_mi2()

    def reload_f(self):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            import mod_andrews
            return reload(mod_andrews)
        else: pass

    def limpar_arquivo(self):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            return os.remove('Dados.xlsx')
        else: pass

    def limpar_caminho(self):
        local = os.getcwd()
        if os.path.isfile(local + '/caminho.txt'):
            return os.remove('caminho.txt')
        else: pass

class Levenspiel_MP2(Screen):
    pass

class Aiba_Shoda_Nagatani_MP2(Screen):
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content_1 = LoadDialog(load=self.load, cancel=self.card)
        self._popup = Popup(title="Load file", content=content_1,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        arq_txt = open("caminho.txt", "a")
        arq_txt.write(f'{os.path.join(path, filename[0])}')

        cwd = os.getcwd()

        path_splited = path.split()
        filename2 = ''
        for i in path_splited:
            filename2 = filename[0].replace(i, '')

        caminho = f'{os.path.join(path, filename[0])}'
        destino = cwd

        shutil.copy2(caminho, destino)
        filename2 = destino + filename2
        file_newname_newfile = os.path.join(destino, 'Dados.xlsx')
        shutil.move(filename2, file_newname_newfile)

    def card(self):
        local = os.getcwd()

        if os.path.isfile(local + '/caminho.txt'):
            nome = open("caminho.txt", "r")
            nome = nome.read()
            nome = str(nome)

            iniciar_button = MDRoundFlatButton(text= 'Iniciar modelagem', on_release = self.show_result)
            close_button = MDFlatButton(text = 'Cancelar', on_release = self.close_dialog)
            self.dialog = MDDialog(text = f'{nome}',
                               size_hint=(0.5, 1),
                               buttons=[iniciar_button, close_button])
            self.dialog.open()
        self._popup.dismiss()

    def show_result(self, obj):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            content_1_2 = ResultDialog_Mod_Aiba2(cancel2=self.dismiss_popup)
            self._popup = Popup(title="Resultados", content=content_1_2,
                                size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
            self._popup.open()
            self.limpar_caminho()

        else:
            pass

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def model(self):
        import mod_aiba_shoda
        return mod_aiba_shoda.result2()

    def modelgraph(self):
        import mod_aiba_shoda
        return mod_aiba_shoda.plot2()

    def model_prod_graph(self):
        import mod_aiba_shoda
        return mod_aiba_shoda.grafico_produtividade2()

    def model_mi_graph(self):
        import mod_aiba_shoda
        return mod_aiba_shoda.grafico_mi2()

    def reload_f(self):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            import mod_aiba_shoda
            return reload(mod_aiba_shoda)
        else: pass

    def limpar_arquivo(self):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            return os.remove('Dados.xlsx')
        else: pass


    def limpar_caminho(self):
        local = os.getcwd()
        if os.path.isfile(local + '/caminho.txt'):
            return os.remove('caminho.txt')
        else: pass

class Escolha_M3(Screen):
    pass

class Monod_MP3(Screen):
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content_3 = LoadDialog(load=self.load, cancel=self.card)
        self._popup = Popup(title="Load file", content=content_3,
                            size_hint=(0.9, 0.9))
        self._popup.open()


    def load(self, path, filename):
        arq_txt = open("caminho.txt", "a")
        arq_txt.write(f'{os.path.join(path, filename[0])}')

        cwd = os.getcwd()

        path_splited = path.split()
        filename2 =''
        for i in path_splited:
            filename2 = filename[0].replace(i, '')

        caminho = f'{os.path.join(path, filename[0])}'
        destino = cwd

        shutil.copy2(caminho,destino)
        filename2 = destino + filename2
        file_newname_newfile = os.path.join(destino, 'Dados.xlsx')
        shutil.move(filename2, file_newname_newfile)

    def card(self):
        local = os.getcwd()

        if os.path.isfile(local + '/caminho.txt'):
            nome = open("caminho.txt", "r")
            nome = nome.read()
            nome = str(nome)

            iniciar_button = MDRoundFlatButton(text= 'Iniciar modelagem', on_release = self.show_result)
            close_button = MDFlatButton(text = 'Cancelar', on_release = self.close_dialog)
            self.dialog = MDDialog(text = f'{nome}',
                               size_hint=(0.5, 1),
                               buttons=[iniciar_button, close_button])
            self.dialog.open()
        self._popup.dismiss()

    def show_result(self, obj):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            content_1_2 = ResultDialog3(cancel4=self.dismiss_popup)
            self._popup = Popup(title="Resultados", content=content_1_2,
                                size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
            self._popup.open()
            self.limpar_caminho()

        else:
            pass

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def model(self):
        import modelagem
        return modelagem.result3()
    def modelgraph(self):
        import modelagem
        return modelagem.plot3()

    def model_prod_graph(self):
        import modelagem
        return modelagem.grafico_produtividade3()

    def model_mi_graph(self):
        import modelagem
        return modelagem.grafico_mi3()

    def reload_f(self):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            import modelagem
            return reload(modelagem)
        else: pass

    def limpar_arquivo(self):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            return os.remove('Dados.xlsx')
        else: pass

    def limpar_caminho(self):
        local = os.getcwd()
        if os.path.isfile(local + '/caminho.txt'):
            return os.remove('caminho.txt')
        else: pass

class Moser_MP3(Screen):
    pass

class Tessier_MP3(Screen):
    pass

class Andrews_MP3(Screen):
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content_1 = LoadDialog(load=self.load, cancel=self.card)
        self._popup = Popup(title="Load file", content=content_1,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        arq_txt = open("caminho.txt", "a")
        arq_txt.write(f'{os.path.join(path, filename[0])}')

        cwd = os.getcwd()

        path_splited = path.split()
        filename2 = ''
        for i in path_splited:
            filename2 = filename[0].replace(i, '')

        caminho = f'{os.path.join(path, filename[0])}'
        destino = cwd

        shutil.copy2(caminho, destino)
        filename2 = destino + filename2
        file_newname_newfile = os.path.join(destino, 'Dados.xlsx')
        shutil.move(filename2, file_newname_newfile)

    def card(self):
        local = os.getcwd()

        if os.path.isfile(local + '/caminho.txt'):
            nome = open("caminho.txt", "r")
            nome = nome.read()
            nome = str(nome)

            iniciar_button = MDRoundFlatButton(text= 'Iniciar modelagem', on_release = self.show_result)
            close_button = MDFlatButton(text = 'Cancelar', on_release = self.close_dialog)
            self.dialog = MDDialog(text = f'{nome}',
                               size_hint=(0.5, 1),
                               buttons=[iniciar_button, close_button])
            self.dialog.open()
        self._popup.dismiss()

    def show_result(self, obj):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            content_1_2 = ResultDialog_Mod_Andrews3(cancel2=self.dismiss_popup)
            self._popup = Popup(title="Resultados", content=content_1_2,
                                size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
            self._popup.open()
            self.limpar_caminho()

        else:
            pass

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def model(self):
        import mod_andrews
        return mod_andrews.result3()

    def modelgraph(self):
        import mod_andrews
        return mod_andrews.plot3()

    def model_prod_graph(self):
        import mod_andrews
        return mod_andrews.grafico_produtividade3()

    def model_mi_graph(self):
        import mod_andrews
        return mod_andrews.grafico_mi3()

    def reload_f(self):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            import mod_andrews
            return reload(mod_andrews)
        else: pass

    def limpar_arquivo(self):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            return os.remove('Dados.xlsx')
        else: pass

    def limpar_caminho(self):
        local = os.getcwd()
        if os.path.isfile(local + '/caminho.txt'):
            return os.remove('caminho.txt')
        else: pass

class Levenspiel_MP3(Screen):
    pass

class Aiba_Shoda_Nagatani_MP3(Screen):
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content_1 = LoadDialog(load=self.load, cancel=self.card)
        self._popup = Popup(title="Load file", content=content_1,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        arq_txt = open("caminho.txt", "a")
        arq_txt.write(f'{os.path.join(path, filename[0])}')

        cwd = os.getcwd()

        path_splited = path.split()
        filename2 = ''
        for i in path_splited:
            filename2 = filename[0].replace(i, '')

        caminho = f'{os.path.join(path, filename[0])}'
        destino = cwd

        shutil.copy2(caminho, destino)
        filename2 = destino + filename2
        file_newname_newfile = os.path.join(destino, 'Dados.xlsx')
        shutil.move(filename2, file_newname_newfile)

    def card(self):
        local = os.getcwd()

        if os.path.isfile(local + '/caminho.txt'):
            nome = open("caminho.txt", "r")
            nome = nome.read()
            nome = str(nome)

            iniciar_button = MDRoundFlatButton(text= 'Iniciar modelagem', on_release = self.show_result)
            close_button = MDFlatButton(text = 'Cancelar', on_release = self.close_dialog)
            self.dialog = MDDialog(text = f'{nome}',
                               size_hint=(0.5, 1),
                               buttons=[iniciar_button, close_button])
            self.dialog.open()
        self._popup.dismiss()

    def show_result(self, obj):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            content_1_2 = ResultDialog_Mod_Aiba3(cancel2=self.dismiss_popup)
            self._popup = Popup(title="Resultados", content=content_1_2,
                                size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
            self._popup.open()
            self.limpar_caminho()

        else:
            pass

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def model(self):
        import mod_aiba_shoda
        return mod_aiba_shoda.result3()

    def modelgraph(self):
        import mod_aiba_shoda
        return mod_aiba_shoda.plot3()

    def model_prod_graph(self):
        import mod_aiba_shoda
        return mod_aiba_shoda.grafico_produtividade3()

    def model_mi_graph(self):
        import mod_aiba_shoda
        return mod_aiba_shoda.grafico_mi3()

    def reload_f(self):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            import mod_aiba_shoda
            return reload(mod_aiba_shoda)
        else: pass

    def limpar_arquivo(self):
        local = os.getcwd()
        if os.path.isfile(local + '/Dados.xlsx'):
            return os.remove('Dados.xlsx')
        else: pass

    def limpar_caminho(self):
        local = os.getcwd()
        if os.path.isfile(local + '/caminho.txt'):
            return os.remove('caminho.txt')
        else: pass

class Simulacao(Screen):
    pass

class Escolha_S1(Screen):
    pass

class Monod_SP1(Screen):
    def p_s1(self):
        s1_t = self.ids.t1
        s1_cxi = self.ids.cx1
        s1_csi = self.ids.cs1
        s1_mimax = self.ids.mimax1
        s1_ks = self.ids.ks1
        s1_yxs = self.ids.yxs1
        s1_kd = self.ids.kd1
        s1_alfa = self.ids.alfa1

        s1_t = s1_t.text
        s1_cxi = s1_cxi.text
        s1_csi = s1_csi.text
        s1_mimax = s1_mimax.text
        s1_ks = s1_ks.text
        s1_yxs = s1_yxs.text
        s1_kd = s1_kd.text
        s1_alfa = s1_alfa.text


        dados_excel = [float(s1_t), float(s1_cxi), float(s1_csi), float(s1_mimax),
             float(s1_ks), float(s1_yxs), float(s1_kd), float(s1_alfa)]
        df_concents_monod_s1 = pd.DataFrame(
            dados_excel)
        with pd.ExcelWriter('Parâmetros_Monod_Sim.xlsx') as writer:
            df_concents_monod_s1.to_excel(writer, sheet_name="Output_concent")
            writer.save()


    def dismiss_popup(self):
        self._popup.dismiss()

    def show_result(self):
        content_sim_monod_1 = ResultDialog_Sim1(cancel5=self.dismiss_popup)
        self._popup = Popup(title="Resultados", content=content_sim_monod_1,
                            size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
        self._popup.open()

    def simu_graph(self):
        import sim_monod
        return sim_monod.plot_sim_monod1()

    def simu_prod_graph(self):
        import sim_monod
        return sim_monod.grafico_produtividade_s1()

    def simu_mi_graph(self):
        import sim_monod
        return sim_monod.mi_monod_s1()

    def dados(self):
        import sim_monod
        return sim_monod.save_s1()

    def reload_f(self):
        import sim_monod
        return reload(sim_monod)

class Moser_SP1(Screen):
    pass

class Tessier_SP1(Screen):
    pass

class Andrews_SP1(Screen):
    def p_s1(self):
        s1_t = self.ids.t1
        s1_cxi = self.ids.cx1
        s1_csi = self.ids.cs1
        s1_mimax = self.ids.mimax1
        s1_ks = self.ids.ks1
        s1_ki = self.ids.ki1
        s1_yxs = self.ids.yxs1
        s1_kd = self.ids.kd1
        s1_alfa = self.ids.alfa1

        s1_t = s1_t.text
        s1_cxi = s1_cxi.text
        s1_csi = s1_csi.text
        s1_mimax = s1_mimax.text
        s1_ks = s1_ks.text
        s1_ki = s1_ki.text
        s1_yxs = s1_yxs.text
        s1_kd = s1_kd.text
        s1_alfa = s1_alfa.text

        dados_excel = [float(s1_t), float(s1_cxi), float(s1_csi), float(s1_mimax),
             float(s1_ks), float(s1_ki), float(s1_yxs), float(s1_kd), float(s1_alfa)]
        df_concents_andrews_s1 = pd.DataFrame(
            dados_excel)
        with pd.ExcelWriter('Parâmetros_Andrews_Sim.xlsx') as writer:
            df_concents_andrews_s1.to_excel(writer, sheet_name="Output_concent")
            writer.save()

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_result(self):
        content_sim_andrews_1 = ResultDialog_Andrews_Sim1(cancel5=self.dismiss_popup)
        self._popup = Popup(title="Resultados", content=content_sim_andrews_1,
                            size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
        self._popup.open()

    def simu_graph(self):
        import sim_andrews
        return sim_andrews.plot_sim_andrews1()

    def simu_prod_graph(self):
        import sim_andrews
        return sim_andrews.grafico_produtividade_s1()

    def simu_mi_graph(self):
        import sim_andrews
        return sim_andrews.mi_andrews_s1()

    def dados(self):
        import sim_andrews
        return sim_andrews.save_s1()

    def reload_f(self):
        import sim_andrews
        return reload(sim_andrews)

class Levenspiel_SP1(Screen):
    pass

class Aiba_Shoda_Nagatani_SP1(Screen):
    def p_s1(self):
        s1_t = self.ids.t1
        s1_cxi = self.ids.cx1
        s1_csi = self.ids.cs1
        s1_mimax = self.ids.mimax1
        s1_ks = self.ids.ks1
        s1_ki = self.ids.ki1
        s1_yxs = self.ids.yxs1
        s1_kd = self.ids.kd1
        s1_alfa = self.ids.alfa1

        s1_t = s1_t.text
        s1_cxi = s1_cxi.text
        s1_csi = s1_csi.text
        s1_mimax = s1_mimax.text
        s1_ks = s1_ks.text
        s1_ki = s1_ki.text
        s1_yxs = s1_yxs.text
        s1_kd = s1_kd.text
        s1_alfa = s1_alfa.text

        dados_excel = [float(s1_t), float(s1_cxi), float(s1_csi), float(s1_mimax),
             float(s1_ks), float(s1_ki), float(s1_yxs), float(s1_kd), float(s1_alfa)]
        df_concents_aiba_s1 = pd.DataFrame(
            dados_excel)
        with pd.ExcelWriter('Parâmetros_Aiba_Sim.xlsx') as writer:
            df_concents_aiba_s1.to_excel(writer, sheet_name="Output_concent")
            writer.save()


    def dismiss_popup(self):
        self._popup.dismiss()

    def show_result(self):
        content_sim_aiba_1 = ResultDialog_Aiba_Sim1(cancel5=self.dismiss_popup)
        self._popup = Popup(title="Resultados", content=content_sim_aiba_1,
                            size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
        self._popup.open()

    def simu_graph(self):
        import sim_aiba_shoda
        return sim_aiba_shoda.plot_sim_aiba1()

    def simu_prod_graph(self):
        import sim_aiba_shoda
        return sim_aiba_shoda.grafico_produtividade_s1()

    def simu_mi_graph(self):
        import sim_aiba_shoda
        return sim_aiba_shoda.mi_aiba_s1()

    def dados(self):
        import sim_aiba_shoda
        return sim_aiba_shoda.save_s1()

    def reload_f(self):
        import sim_aiba_shoda
        return reload(sim_aiba_shoda)

class Escolha_S2(Screen):
    pass

class Monod_SP2(Screen):
    def p_s2(self):
        s2_t = self.ids.t2
        s2_cxi = self.ids.cx2
        s2_csi = self.ids.cs2
        s2_mimax = self.ids.mimax2
        s2_ks = self.ids.ks2
        s2_yxs = self.ids.yxs2
        s2_kd = self.ids.kd2
        s2_beta = self.ids.beta2

        s2_t = float(s2_t.text)
        s2_cxi = float(s2_cxi.text)
        s2_csi = float(s2_csi.text)
        s2_mimax = float(s2_mimax.text)
        s2_ks = float(s2_ks.text)
        s2_yxs = float(s2_yxs.text)
        s2_kd = float(s2_kd.text)
        s2_beta = float(s2_beta.text)

        dados_excel = [float(s2_t), float(s2_cxi), float(s2_csi), float(s2_mimax),
             float(s2_ks), float(s2_yxs), float(s2_kd), float(s2_beta)]

        df_concents_monod_s1 = pd.DataFrame(
           dados_excel)
        with pd.ExcelWriter('Parâmetros_Monod_Sim.xlsx') as writer:
            df_concents_monod_s1.to_excel(writer, sheet_name="Output_concent")
            writer.save()

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_result(self):
        content_sim_monod_2 = ResultDialog_Sim2(cancel6=self.dismiss_popup)
        self._popup = Popup(title="Resultados", content=content_sim_monod_2,
                            size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
        self._popup.open()

    def simu_graph(self):
        import sim_monod
        return sim_monod.plot_sim_monod2()

    def simu_prod_graph(self):
        import sim_monod
        return sim_monod.grafico_produtividade_s2()

    def simu_mi_graph(self):
        import sim_monod
        return sim_monod.mi_monod_s2()

    def dados(self):
        import sim_monod
        return sim_monod.save_s2()

    def reload_f(self):
        import sim_monod
        return reload(sim_monod)

class Moser_SP2(Screen):
    pass

class Tessier_SP2(Screen):
    pass

class Andrews_SP2(Screen):
    def p_s2(self):
        s2_t = self.ids.t2
        s2_cxi = self.ids.cx2
        s2_csi = self.ids.cs2
        s2_mimax = self.ids.mimax2
        s2_ks = self.ids.ks2
        s2_ki = self.ids.ki2
        s2_yxs = self.ids.yxs2
        s2_kd = self.ids.kd2
        s2_beta = self.ids.beta2

        s2_t = s2_t.text
        s2_cxi = s2_cxi.text
        s2_csi = s2_csi.text
        s2_mimax = s2_mimax.text
        s2_ks = s2_ks.text
        s2_ki = s2_ki.text
        s2_yxs = s2_yxs.text
        s2_kd = s2_kd.text
        s2_beta = s2_beta.text

        dados_excel = [float(s2_t), float(s2_cxi), float(s2_csi), float(s2_mimax),
             float(s2_ks), float(s2_ki), float(s2_yxs), float(s2_kd), float(s2_beta)]
        df_concents_andrews_s2 = pd.DataFrame(
            dados_excel)
        with pd.ExcelWriter('Parâmetros_Andrews_Sim.xlsx') as writer:
            df_concents_andrews_s2.to_excel(writer, sheet_name="Output_concent")
            writer.save()


    def dismiss_popup(self):
        self._popup.dismiss()

    def show_result(self):
        content_sim_andrews_2 = ResultDialog_Andrews_Sim2(cancel6=self.dismiss_popup)
        self._popup = Popup(title="Resultados", content=content_sim_andrews_2,
                            size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
        self._popup.open()

    def simu_graph(self):
        import sim_andrews
        return sim_andrews.plot_sim_andrews2()

    def simu_prod_graph(self):
        import sim_andrews
        return sim_andrews.grafico_produtividade_s2()

    def simu_mi_graph(self):
        import sim_andrews
        return sim_andrews.mi_andrews_s2()

    def dados(self):
        import sim_andrews
        return sim_andrews.save_s2()

    def reload_f(self):
        import sim_andrews
        return reload(sim_andrews)

class Levenspiel_SP2(Screen):
    pass

class Aiba_Shoda_Nagatani_SP2(Screen):
    def p_s2(self):
        s2_t = self.ids.t2
        s2_cxi = self.ids.cx2
        s2_csi = self.ids.cs2
        s2_mimax = self.ids.mimax2
        s2_ks = self.ids.ks2
        s2_ki = self.ids.ki2
        s2_yxs = self.ids.yxs2
        s2_kd = self.ids.kd2
        s2_beta = self.ids.beta2

        s2_t = s2_t.text
        s2_cxi = s2_cxi.text
        s2_csi = s2_csi.text
        s2_mimax = s2_mimax.text
        s2_ks = s2_ks.text
        s2_ki = s2_ki.text
        s2_yxs = s2_yxs.text
        s2_kd = s2_kd.text
        s2_beta = s2_beta.text

        dados_excel = [float(s2_t), float(s2_cxi), float(s2_csi), float(s2_mimax),
             float(s2_ks), float(s2_ki), float(s2_yxs), float(s2_kd), float(s2_beta)]
        df_concents_aiba_s2 = pd.DataFrame(
            dados_excel)
        with pd.ExcelWriter('Parâmetros_Aiba_Sim.xlsx') as writer:
            df_concents_aiba_s2.to_excel(writer, sheet_name="Output_concent")
            writer.save()


    def dismiss_popup(self):
        self._popup.dismiss()

    def show_result(self):
        content_sim_aiba_2 = ResultDialog_Aiba_Sim2(cancel6=self.dismiss_popup)
        self._popup = Popup(title="Resultados", content=content_sim_aiba_2,
                            size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
        self._popup.open()

    def simu_graph(self):
        import sim_aiba_shoda
        return sim_aiba_shoda.plot_sim_aiba2()

    def simu_prod_graph(self):
        import sim_aiba_shoda
        return sim_aiba_shoda.grafico_produtividade_s2()

    def simu_mi_graph(self):
        import sim_aiba_shoda
        return sim_aiba_shoda.mi_aiba_s2()

    def dados(self):
        import sim_aiba_shoda
        return sim_aiba_shoda.save_s2()

    def reload_f(self):
        import sim_aiba_shoda
        return reload(sim_aiba_shoda)

class Escolha_S3(Screen):
    pass

class Monod_SP3(Screen):
    def p_s3(self):
        s3_t = self.ids.t3
        s3_cxi = self.ids.cx3
        s3_csi = self.ids.cs3
        s3_mimax = self.ids.mimax3
        s3_ks = self.ids.ks3
        s3_yxs = self.ids.yxs3
        s3_kd = self.ids.kd3
        s3_alfa = self.ids.alfa3
        s3_beta = self.ids.beta3

        s3_t = float(s3_t.text)
        s3_cxi = float(s3_cxi.text)
        s3_csi = float(s3_csi.text)
        s3_mimax = float(s3_mimax.text)
        s3_ks = float(s3_ks.text)
        s3_yxs = float(s3_yxs.text)
        s3_kd = float(s3_kd.text)
        s3_alfa = float(s3_alfa.text)
        s3_beta = float(s3_beta.text)

        dados_excel = [float(s3_t), float(s3_cxi), float(s3_csi), float(s3_mimax),
             float(s3_ks), float(s3_yxs), float(s3_kd), float(s3_alfa), float(s3_beta)]

        df_concents_monod_s1 = pd.DataFrame(
           dados_excel)
        with pd.ExcelWriter('Parâmetros_Monod_Sim.xlsx') as writer:
            df_concents_monod_s1.to_excel(writer, sheet_name="Output_concent")
            writer.save()

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_result(self):
        content_sim_monod_3 = ResultDialog_Sim3(cancel7=self.dismiss_popup)
        self._popup = Popup(title="Resultados", content=content_sim_monod_3,
                            size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
        self._popup.open()

    def simu_graph(self):
        import sim_monod
        return sim_monod.plot_sim_monod3()

    def simu_prod_graph(self):
        import sim_monod
        return sim_monod.grafico_produtividade_s3()

    def simu_mi_graph(self):
        import sim_monod
        return sim_monod.mi_monod_s3()

    def dados(self):
        import sim_monod
        return sim_monod.save_s3()

    def reload_f(self):
        import sim_monod
        return reload(sim_monod)

class Moser_SP3(Screen):
    pass

class Tessier_SP3(Screen):
    pass

class Andrews_SP3(Screen):
    def p_s3(self):
        s3_t = self.ids.t3
        s3_cxi = self.ids.cx3
        s3_csi = self.ids.cs3
        s3_mimax = self.ids.mimax3
        s3_ks = self.ids.ks3
        s3_ki = self.ids.ki3
        s3_yxs = self.ids.yxs3
        s3_kd = self.ids.kd3
        s3_alfa = self.ids.alfa3
        s3_beta = self.ids.beta3

        s3_t = s3_t.text
        s3_cxi = s3_cxi.text
        s3_csi = s3_csi.text
        s3_mimax = s3_mimax.text
        s3_ks = s3_ks.text
        s3_ki = s3_ki.text
        s3_yxs = s3_yxs.text
        s3_kd = s3_kd.text
        s3_alfa = s3_alfa.text
        s3_beta = s3_beta.text

        dados_excel = [float(s3_t), float(s3_cxi), float(s3_csi), float(s3_mimax),
             float(s3_ks), float(s3_ki), float(s3_yxs), float(s3_kd), float(s3_alfa), float(s3_beta)]
        df_concents_andrews_s3 = pd.DataFrame(
            dados_excel)
        with pd.ExcelWriter('Parâmetros_Andrews_Sim.xlsx') as writer:
            df_concents_andrews_s3.to_excel(writer, sheet_name="Output_concent")
            writer.save()


    def dismiss_popup(self):
        self._popup.dismiss()

    def show_result(self):
        content_sim_andrews_3 = ResultDialog_Andrews_Sim3(cancel7=self.dismiss_popup)
        self._popup = Popup(title="Resultados", content=content_sim_andrews_3,
                            size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
        self._popup.open()

    def simu_graph(self):
        import sim_andrews
        return sim_andrews.plot_sim_andrews3()

    def simu_prod_graph(self):
        import sim_andrews
        return sim_andrews.grafico_produtividade_s3()

    def simu_mi_graph(self):
        import sim_andrews
        return sim_andrews.mi_andrews_s3()

    def dados(self):
        import sim_andrews
        return sim_andrews.save_s3()

    def reload_f(self):
        import sim_andrews
        return reload(sim_andrews)

class Levenspiel_SP3(Screen):
    pass

class Aiba_Shoda_Nagatani_SP3(Screen):
    def p_s3(self):
        s3_t = self.ids.t3
        s3_cxi = self.ids.cx3
        s3_csi = self.ids.cs3
        s3_mimax = self.ids.mimax3
        s3_ks = self.ids.ks3
        s3_ki = self.ids.ki3
        s3_yxs = self.ids.yxs3
        s3_kd = self.ids.kd3
        s3_alfa = self.ids.alfa3
        s3_beta = self.ids.beta3

        s3_t = s3_t.text
        s3_cxi = s3_cxi.text
        s3_csi = s3_csi.text
        s3_mimax = s3_mimax.text
        s3_ks = s3_ks.text
        s3_ki = s3_ki.text
        s3_yxs = s3_yxs.text
        s3_kd = s3_kd.text
        s3_alfa = s3_alfa.text
        s3_beta = s3_beta.text

        dados_excel = [float(s3_t), float(s3_cxi), float(s3_csi), float(s3_mimax),
             float(s3_ks), float(s3_ki), float(s3_yxs), float(s3_kd), float(s3_alfa), float(s3_beta)]
        df_concents_aiba_s3 = pd.DataFrame(
            dados_excel)
        with pd.ExcelWriter('Parâmetros_Aiba_Sim.xlsx') as writer:
            df_concents_aiba_s3.to_excel(writer, sheet_name="Output_concent")
            writer.save()


    def dismiss_popup(self):
        self._popup.dismiss()

    def show_result(self):
        content_sim_aiba_3 = ResultDialog_Aiba_Sim3(cancel7=self.dismiss_popup)
        self._popup = Popup(title="Resultados", content=content_sim_aiba_3,
                            size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
        self._popup.open()

    def simu_graph(self):
        import sim_aiba_shoda
        return sim_aiba_shoda.plot_sim_aiba3()

    def simu_prod_graph(self):
        import sim_aiba_shoda
        return sim_aiba_shoda.grafico_produtividade_s3()

    def simu_mi_graph(self):
        import sim_aiba_shoda
        return sim_aiba_shoda.mi_aiba_s3()

    def dados(self):
        import sim_aiba_shoda
        return sim_aiba_shoda.save_s3()

    def reload_f(self):
        import sim_aiba_shoda
        return reload(sim_aiba_shoda)

class WindowManager(ScreenManager):
    pass


class Processo_FermentativoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        screen = Builder.load_file('main.kv')
        return screen

    def on_stop(self):
        local = os.getcwd()

        if os.path.isfile(local + '/Dados.xlsx'):
            os.remove('Dados.xlsx')
        if os.path.isfile(local + '/Parâmetros_Monod_Sim.xlsx'):
            os.remove('Parâmetros_Monod_Sim.xlsx')
        if os.path.isfile(local + '/Parâmetros_Andrews_Sim.xlsx'):
            os.remove('Parâmetros_Andrews_Sim.xlsx')
        if os.path.isfile(local + '/Parâmetros_Aiba_Sim.xlsx'):
            os.remove('Parâmetros_Aiba_Sim.xlsx')
if __name__ == '__main__':
    Processo_FermentativoApp().run()