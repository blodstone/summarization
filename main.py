from system.opts import Opts
from module.auto_module_generator import AutoModuleGenerator
from application import Application


if __name__ == '__main__':
    opts = Opts()
    app = Application()
    # autoModuleGen = AutoModuleGenerator('train')
    # autoModuleGen.set_up_context(opts.args)
    # train_modules = autoModuleGen.gen_modules()
    #
    # autoModuleGen = AutoModuleGenerator('dev')
    # autoModuleGen.set_up_context(opts.args)
    # dev_modules = autoModuleGen.gen_modules()

    autoModuleGen = AutoModuleGenerator('test')
    autoModuleGen.set_up_context(opts.args)
    test_modules = autoModuleGen.gen_modules()

    app.run_modules([*test_modules])
