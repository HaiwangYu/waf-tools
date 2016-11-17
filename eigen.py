import os
import os.path as osp
from waflib.Configure import conf

def options(opt):
    opt = opt.add_option_group('Eigen Options')
    opt.add_option('--with-eigen', type='string',
                   help="enable Eigen3 with 'yes' or specify installation location")


@conf
def check_eigen(ctx, mandatory=True):
    instdir = ctx.options.with_eigen
    if instdir is None:
        return

    if instdir.lower() in ['yes','true','on']:
        ctx.start_msg('Checking for Eigen in PKG_CONFIG_PATH')
        # note: Eigen puts its eigen3.pc file under share as there is
        # no lib.  Be sure your PKG_CONFIG_PATH reflects this.
        ctx.check_cfg(package='eigen3',  uselib_store='EIGEN', args='--cflags --libs', mandatory=mandatory)
    else:
        ctx.start_msg('Checking for Eigen in %s' % instdir)
        ctx.env.INCLUDES_EIGEN = [ osp.join(instdir,'include/eigen3') ]

    ctx.check(header_name="Eigen/Dense", use='EIGEN', mandatory=mandatory)
    ctx.end_msg(ctx.env.INCLUDES_EIGEN[0], mandatory=mandatory)

def configure(cfg):
    cfg.check_eigen()
