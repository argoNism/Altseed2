from . import CppBindingGenerator as cbg
import ctypes

from .common import *

#FFTWindow = cbg.Enum('Altseed', 'FFTWindow')
#with FFTWindow as enum:
#    enum.brief = cbg.Description()
#    enum.brief.add('ja', '音のスペクトル解析に使用する窓関数')
#    enum.add('Rectangular', 0)
#    enum.add('Triangle', 1)
#    enum.add('Hamming', 2)
#    enum.add('Hanning', 3)
#    enum.add('Blackman', 4)
#    enum.add('BlackmanHarris', 5)

Sound = cbg.Class('Altseed', 'Sound')
with Sound as class_:
    class_.brief = cbg.Description()
    class_.brief.add('ja', '音源のクラス')

    with class_.add_func('Load') as func:
        func.brief = cbg.Description()
        class_.brief.add('ja', '音声ファイルを読み込む')
        func.is_static = True
        with func.add_arg(ctypes.c_wchar_p, 'path') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('読み込む音声ファイルのパス')
        with func.add_arg(bool, 'isDecompressed') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('音を再生する前にデータを全て解凍するか?')
        func.return_value.type_ = Sound
        func.return_value.brief = cbg.Description()
        func.return_value.brief.add('ja', '読み込んだ音源データ')

    with class_.add_property(float, 'LoopStartingPoint') as prop:
        prop.brief = cbg.Description()
        prop.brief.add('ja', 'ループ開始地点(秒)を取得または設定する')
        prop.has_getter = True
        prop.has_setter = True

    with class_.add_property(float, 'LoopEndPoint') as prop:
        prop.brief = cbg.Description()
        prop.brief.add('ja', 'ループ終了地点(秒)を取得または設定する')
        prop.has_getter = True
        prop.has_setter = True

    with class_.add_property(bool, 'IsLoopingMode') as prop:
        prop.brief = cbg.Description()
        prop.brief.add('ja', 'ループするかどうかを取得または設定する')
        prop.has_getter = True
        prop.has_setter = True

    with class_.add_property(float, 'Length') as prop:
        prop.brief = cbg.Description()
        prop.brief.add('ja', '音源の長さ(秒)を取得する')
        prop.has_getter = True

SoundMixer = cbg.Class('Altseed', 'SoundMixer')
with SoundMixer as class_:

    with class_.add_func('GetInstance') as func:
        func.is_static = True
        func.is_public = False
        func.return_value.type_ = SoundMixer

    with class_.add_func('Play') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', '音を再生する')
        with func.add_arg(Sound, 'sound') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '音源データ')
        func.return_value.type_ = int
        func.return_value.brief = cbg.Description()
        func.return_value.brief.add('ja', '再生中の音のID')

    with class_.add_func('GetIsPlaying') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', '指定した音が再生中であるかを取得する')
        with func.add_arg(int, 'id') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '音のID')
        func.return_value.type_ = bool
        func.return_value.brief = cbg.Description()
        func.return_value.brief.add('ja', 'IDに対応する音が再生中であるか?')

    with class_.add_func('StopAll') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', '再生中の音を全て停止する')

    with class_.add_func('Stop') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', '指定した音の再生を停止する')
        with func.add_arg(int, 'id') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '音のID')

    with class_.add_func('Pause') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', '指定した音の再生を一時停止する')
        with func.add_arg(int, 'id') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '音のID')

    with class_.add_func('Resume') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', '指定した音の再生を再開する')
        with func.add_arg(int, 'id') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '音のID')

    with class_.add_func('Seek') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', '指定した音の再生位置を変更する')
        with func.add_arg(int, 'id') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '音のID')
        with func.add_arg(float, 'position') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '再生位置(秒)')

    with class_.add_func('SetVolume') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', '指定した音の音量を変更する')
        with func.add_arg(int, 'id') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '音のID')
        with func.add_arg(float, 'volume') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '音量(0.0~1.0')

    with class_.add_func('FadeIn') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', '指定した音をフェードインさせる')
        with func.add_arg(int, 'id') as arg:
            arg.brief = cbg.Description()
        with func.add_arg(float, 'second') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', 'フェードインに使用する時間(秒)')

    with class_.add_func('FadeOut') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', '指定した音をフェードアウトさせる')
        with func.add_arg(int, 'id') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '音のID')
        with func.add_arg(float, 'second') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', 'フェードアウトに使用する時間(秒)')

    with class_.add_func('Fade') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', '指定した音の音量を一定時間かけて変更する')
        with func.add_arg(int, 'id') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '音のID')
        with func.add_arg(float, 'second') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', 'フェードに使用する時間(秒)')
        with func.add_arg(float, 'targetedVolume') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '変更後の音量(0.0~1.0)')

    with class_.add_func('GetIsPlaybackSpeedEnabled') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', '再生速度を変更するかを取得する')
        with func.add_arg(int, 'id') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '音のID')
        func.return_value.type_ = bool
        func.return_value.brief = cbg.Description()
        func.return_value.brief.add('ja', '再生速度を変更するか?')

    with class_.add_func('SetIsPlaybackSpeedEnabled') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', '再生速度を変更するかを設定する')
        with func.add_arg(int, 'id') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '音のID')
        with func.add_arg(bool, 'isPlaybackSpeedEnabled') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '再生速度を変更するか?')

    with class_.add_func('GetPlaybackSpeed') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', '再生速度を取得する')
        with func.add_arg(int, 'id') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '音のID')
        func.return_value.type_ = float
        func.return_value.brief = cbg.Description()
        func.return_value.brief.add('ja', '本来の速度の何倍で再生されているか?')

    with class_.add_func('SetPlaybackSpeed') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', '再生速度を設定する')
        with func.add_arg(int, 'id') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '音のID')
        with func.add_arg(float, 'playbackSpeed') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '変更後の再生速度')

    with class_.add_func('GetPanningPosition') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', 'パン位置を取得する')
        with func.add_arg(int, 'id') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '音のID')
        func.return_value.type_ = float
        func.return_value.brief = cbg.Description()
        func.return_value.brief.add('ja', 'パン位置 : 0.0で中央, -1.0で左, 1.0で右')

    with class_.add_func('SetPanningPosition') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', 'パン位置を設定する')
        with func.add_arg(int, 'id') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '音のID')
        with func.add_arg(float, 'panningPosition')as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', 'パン位置 : 0.0で中央, -1.0で左, 1.0で右')

    with class_.add_func('GetPlaybackPercent') as func:
        func.brief = cbg.Description()
        func.brief.add('ja', '指定した音の再生位置を0~1で取得する')
        with func.add_arg(int, 'id') as arg:
            arg.brief = cbg.Description()
            arg.brief.add('ja', '音のID')
        func.return_value.type_ = float
        func.return_value.brief = cbg.Description()
        func.return_value.brief.add('ja', '現在の再生位置')