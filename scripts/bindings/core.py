from . import CppBindingGenerator as cbg
import ctypes
import sys

from .common import *

Configuration = cbg.Class('Altseed', 'Configuration')
with Configuration as class_:
    class_.brief = cbg.Description()
    class_.brief.add('ja', 'Coreを初期化する際の設定を保持すクラス')

    class_.add_constructor()

    with class_.add_property(bool, 'IsFullscreenMode') as prop:
        prop.brief = cbg.Description()
        prop.brief.add('ja', '全画面モードかどうかを取得または設定します。')
        prop.has_getter = True
        prop.has_setter = True
    
    with class_.add_property(bool, 'IsResizable') as prop:
        prop.brief = cbg.Description()
        prop.brief.add('ja', '画面サイズ可変かどうかを取得または設定します。')
        prop.has_getter = True
        prop.has_setter = True

    with class_.add_property(bool, 'EnabledConsoleLogging') as prop:
        prop.brief = cbg.Description()
        prop.brief.add('ja', 'ログをコンソールに出力するかどうかを取得または設定します。')
        prop.has_getter = True
        prop.has_setter = True

    with class_.add_property(bool, 'EnabledFileLogging') as prop:
        prop.brief = cbg.Description()
        prop.brief.add('ja', 'ログをファイルに出力するかどうかを取得または設定します。')
        prop.has_getter = True
        prop.has_setter = True
    
    with class_.add_property(ctypes.c_wchar_p, 'LogFilename') as prop:
        prop.brief = cbg.Description()
        prop.brief.add('ja', 'ログファイル名を取得または設定します。')
        prop.has_getter = True
        prop.has_setter = True

FramerateMode = cbg.Enum('Altseed', 'FramerateMode')
with FramerateMode as enum_:
    enum_.brief = cbg.Description()
    enum_.brief.add('ja', 'フレームレートモード')
    enum_.add('Variable')
    enum_.add('Constant')

Core = cbg.Class('Altseed', 'Core')
with Core as class_:
    class_.brief = cbg.Description()
    class_.brief.add('ja', 'C++のCoreとの仲介を担うクラス')
    class_.is_public = False
    with class_.add_func('Initialize') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', '初期化処理を行います。')
        with func.add_arg(ctypes.c_wchar_p, 'title') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', 'ウィンドウの左上に表示されるウィンドウん名')
        with func.add_arg(int, 'width') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', 'ウィンドウの横幅')
        with func.add_arg(int, 'height') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', 'ウィンドウの縦幅')
        with func.add_arg(Configuration, 'config') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '初期化時の設定')
        func.return_value.type_ = bool
        func.return_value.brief = cbg.Description()
        func.return_value.brief.add('ja', '初期化処理がうまくいったらtrue，それ以外でfalse')
        func.is_static = True

    with class_.add_func('DoEvent') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', 'イベントを実行します。')
        func.return_value.type_ = bool
        func.return_value.brief = cbg.Description()
        func.return_value.brief.add('ja', 'イベントが進行出来たらtrue，それ以外でfalse')

    with class_.add_func('Terminate') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', '終了処理を行います。')
        func.is_static = True

    with class_.add_func('GetInstance') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', 'インスタンスを取得します。')
        func.return_value.type_ = Core
        func.return_value.brief = cbg.Description()
        func.return_value.brief.add('ja', '使用するインスタンス')
        func.is_public = False
        func.is_static = True

    with class_.add_property(float, 'DeltaSecond') as prop_:
        prop_.brief = cbg.Description()
        prop_.brief.add('ja', '前のフレームからの経過時間(秒)を取得します。')
        prop_.has_getter = True
        prop_.has_setter = False

    with class_.add_property(float, 'CurrentFPS') as prop_:
        prop_.brief = cbg.Description()
        prop_.brief.add('ja', '現在のFPSを取得します。')
        prop_.has_getter = True
        prop_.has_setter = False

    with class_.add_property(float, 'TargetFPS') as prop_:
        prop_.brief = cbg.Description()
        prop_.brief.add('ja', '目標のFPSを取得または設定します。')
        prop_.has_getter = True
        prop_.has_setter = True

    with class_.add_property(FramerateMode, 'FramerateMode') as prop_:
        prop_.brief = cbg.Description()
        prop_.brief.add('ja', 'フレームレートモードを取得または設定します。デフォルトでは可変フレームレートです。')
        prop_.has_getter = True
        prop_.has_setter = True
