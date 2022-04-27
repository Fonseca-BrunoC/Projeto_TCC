from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import os
import shutil
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class LoadDialog(MDBoxLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class ResultDialog1(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.p = MP1().model()
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
        self.g = MP1().modelgraph()
        return self.g

    cancel2 = ObjectProperty(None)

class ResultDialog2(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.p = MP2().model()
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
        self.g = MP2().modelgraph()
        return self.g

    cancel3 = ObjectProperty(None)

class ResultDialog3(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.p = MP3().model()
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
        self.g = MP3().modelgraph()
        return self.g


    cancel4 = ObjectProperty(None)

class Home(Screen):
    pass

class Modelagem(Screen):
    pass

class MP1(Screen):
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content_1 = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content_1,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
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

    def show_result(self):
        content_1_2 = ResultDialog1(cancel2=self.dismiss_popup)
        self._popup = Popup(title="Resultados", content=content_1_2,
                            size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
        self._popup.open()

    def model(self):
        import modelagem
        return modelagem.result1()

    def modelgraph(self):
        import modelagem
        return modelagem.plot1()

class MP2(Screen):
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content_2 = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content_2,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
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

    def show_result(self):
        content_2_2 = ResultDialog2(cancel3=self.dismiss_popup)
        self._popup = Popup(title="Resultados", content=content_2_2,
                            size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
        self._popup.open()

    def model(self):
        import modelagem
        return modelagem.result2()

    def modelgraph(self):
        import modelagem
        return modelagem.plot2()

class MP3(Screen):
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content_3 = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content_3,
                            size_hint=(0.9, 0.9))
        self._popup.open()


    def load(self, path, filename):
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

    def show_result(self):
        content_3_2 = ResultDialog3(cancel4=self.dismiss_popup)
        self._popup = Popup(title="Resultados", content=content_3_2,
                           size_hint=(0.9, 0.9), background='lightgray', title_color=(0, 0, 0, 1))
        self._popup.open()


    def model(self):
        import modelagem
        return modelagem.result3()
    def modelgraph(self):
        import modelagem
        return modelagem.plot3()

class Simulacao(Screen):
    pass

class SP1(Screen):
    def sol1(self):
        import sim

        s1_t = self.ids.t1
        s1_cxi = self.ids.cx1
        s1_csi = self.ids.cs1
        s1_mimax = self.ids.mimax1
        s1_ks = self.ids.ks1
        s1_yxs = self.ids.yxs1
        s1_kd = self.ids.kd1
        s1_alfa = self.ids.alfa1

        s1_t = float(s1_t.text)
        s1_cxi = float(s1_cxi.text)
        s1_csi = float(s1_csi.text)
        s1_mimax = float(s1_mimax.text)
        s1_ks = float(s1_ks.text)
        s1_yxs = float(s1_yxs.text)
        s1_kd = float(s1_kd.text)
        s1_alfa = float(s1_alfa.text)

        t = np.linspace(0, s1_t, int(s1_t * 10))
        Ci = s1_cxi, s1_csi, 0
        s1_p = s1_mimax, s1_ks, s1_yxs, s1_kd, s1_alfa
        s1_p = tuple(s1_p)
        sol = odeint(sim.edo, Ci, t, args = s1_p)

        Cx = sol[:, 0]
        Cs = sol[:, 1]
        Cp = sol[:, 2]

        f_S1 = plt.figure()
        ax = f_S1.add_subplot(111)
        plt.rc('axes', titlesize=15)
        plt.rc('axes', labelsize=10)
        func = ax.plot(t, Cx, 'r-', linewidth=2, label='Cx')
        func2 = ax.plot(t, Cs, 'b-', linewidth=2, label='Cs')
        func3 = ax.plot(t, Cp, 'g-', linewidth=2, label='Cp')
        ax.set_title("SIMULAÇÃO - PRODUTO ASSOCIADO AO CRESCIMENTO", weight='bold')
        ax.set_xlabel('Tempo (h)', weight='bold')
        ax.set_ylabel('Concentração (g/L)', weight='bold')
        ax.grid(True)
        ax.legend(loc='upper center', ncol=2, shadow=True)
        f_S1.set_figheight(5)
        f_S1.set_figwidth(8)
        return plt.show()


class SP2(Screen):
    def sol2(self):
        import sim

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

        t = np.linspace(0, s2_t, int(s2_t * 10))
        Ci = s2_cxi, s2_csi, 0
        s2_p = s2_mimax, s2_ks, s2_yxs, s2_kd, s2_beta
        s2_p = tuple(s2_p)
        sol = odeint(sim.edo2, Ci, t, args = s2_p)

        Cx = sol[:, 0]
        Cs = sol[:, 1]
        Cp = sol[:, 2]

        f_S2 = plt.figure()
        ax = f_S2.add_subplot(111)
        plt.rc('axes', titlesize=15)
        plt.rc('axes', labelsize=10)
        func = ax.plot(t, Cx, 'r-', linewidth=2, label='Cx')
        func2 = ax.plot(t, Cs, 'b-', linewidth=2, label='Cs')
        func3 = ax.plot(t, Cp, 'g-', linewidth=2, label='Cp')
        ax.set_title("SIMULAÇÃO - PRODUTO ASSOCIADO AO CRESCIMENTO", weight='bold')
        ax.set_xlabel('Tempo (h)', weight='bold')
        ax.set_ylabel('Concentração (g/L)', weight='bold')
        ax.grid(True)
        ax.legend(loc='upper center', ncol=2, shadow=True)
        f_S2.set_figheight(5)
        f_S2.set_figwidth(8)
        return plt.show()

class SP3(Screen):
    def sol3(self):
        import sim

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

        t = np.linspace(0, s3_t, int(s3_t * 10))
        Ci = s3_cxi, s3_csi, 0
        s3_p = s3_mimax, s3_ks, s3_yxs, s3_kd, s3_alfa, s3_beta
        s3_p = tuple(s3_p)
        sol = odeint(sim.edo3, Ci, t, args = s3_p)

        Cx = sol[:, 0]
        Cs = sol[:, 1]
        Cp = sol[:, 2]

        f_S3 = plt.figure()
        ax = f_S3.add_subplot(111)
        plt.rc('axes', titlesize=15)
        plt.rc('axes', labelsize=10)
        func = ax.plot(t, Cx, 'r-', linewidth=2, label='Cx')
        func2 = ax.plot(t, Cs, 'b-', linewidth=2, label='Cs')
        func3 = ax.plot(t, Cp, 'g-', linewidth=2, label='Cp')
        ax.set_title("SIMULAÇÃO - PRODUTO ASSOCIADO AO CRESCIMENTO", weight='bold')
        ax.set_xlabel('Tempo (h)', weight='bold')
        ax.set_ylabel('Concentração (g/L)', weight='bold')
        ax.grid(True)
        ax.legend(loc='upper center', ncol=2, shadow=True)
        f_S3.set_figheight(5)
        f_S3.set_figwidth(8)
        return plt.show()

class WindowManager(ScreenManager):
    pass


class Processo_FermentativoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        screen = Builder.load_file('main.kv')
        return screen

    def on_stop(self):
        return os.remove('Dados.xlsx')

if __name__ == '__main__':
    Processo_FermentativoApp().run()