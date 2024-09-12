import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import ProgressBar, IndeterminateProgressBar, SettingCardGroup, \
    FluentIcon, HyperlinkCard, ImageLabel

from one_dragon.base.operation.one_dragon_env_context import OneDragonEnvContext
from one_dragon.gui.component.column_widget import ColumnWidget
from one_dragon.gui.component.cv2_image import Cv2Image
from one_dragon.gui.component.interface.vertical_scroll_interface import VerticalScrollInterface
from one_dragon.gui.component.log_display_card import LogDisplayCard
from one_dragon.gui.install_card.all_install_card import AllInstallCard
from one_dragon.gui.install_card.code_install_card import CodeInstallCard
from one_dragon.gui.install_card.git_install_card import GitInstallCard
from one_dragon.gui.install_card.python_install_card import PythonInstallCard
from one_dragon.gui.install_card.venv_install_card import VenvInstallCard
from one_dragon.utils import cv2_utils, os_utils
from one_dragon.utils.i18_utils import gt


class LikeInterface(VerticalScrollInterface):

    def __init__(self, ctx: OneDragonEnvContext, parent=None):
        VerticalScrollInterface.__init__(self, object_name='like_interface',
                                         parent=parent, content_widget=None,
                                         nav_text_cn='点赞', nav_icon=FluentIcon.HEART)

    def get_content_widget(self) -> QWidget:
        content = ColumnWidget()

        star_opt = HyperlinkCard(icon=FluentIcon.HOME, title='Star', text='前往',
                                 content='Github主页右上角点一个星星是最简单直接的',
                                 url='https://github.com/DoctorReid/ZenlessZoneZero-OneDragon')
        content.add_widget(star_opt)

        help_opt = HyperlinkCard(icon=FluentIcon.HELP, title='访问Github指南', text='前往',
                                 content='没法访问Github可以查看帮助文档',
                                 url='https://one-dragon.org/other/zh/visit_github.html')
        content.add_widget(help_opt)

        cafe_opt = HyperlinkCard(icon=FluentIcon.CAFE, title='赞赏', text='前往',
                                 content='如果喜欢本项目，你也可以为作者赞助一点维护费用~',
                                 url='https://one-dragon.org/other/zh/like.html')
        content.add_widget(cafe_opt)

        img_label = ImageLabel()
        img = cv2_utils.read_image(os.path.join(os_utils.get_path_under_work_dir('assets', 'ui'), 'sponsor_wechat.png'))
        image = Cv2Image(img)
        img_label.setImage(image)
        img_label.setFixedWidth(250)
        img_label.setFixedHeight(250)
        content.add_widget(img_label)

        content.add_stretch(1)
        return content


    def on_interface_shown(self) -> None:
        VerticalScrollInterface.on_interface_shown(self)

