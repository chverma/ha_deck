import os
import esphome.core as core
import esphome.codegen as cg

CODEOWNERS = ["@buglloc"]

axs15231_ns = cg.esphome_ns.namespace("axs15231")
LVGL_BUILD_FLAGS = [
    "-D LV_USE_DEV_VERSION=1",
    "-D LV_LVGL_H_INCLUDE_SIMPLE=1",
]

async def to_code(config):
    whereami = os.path.realpath(__file__)
    component_dir = os.path.dirname(whereami)

    lv_conf_path = os.path.join(component_dir, 'lv_conf.h')
    core.CORE.add_job(cfg.add_includes, [lv_conf_path])

    cg.add_library("lvgl/lvgl", "^8.3")
    cg.add_platformio_option("build_flags", LVGL_BUILD_FLAGS)
    cg.add_platformio_option("build_flags", ["-D LV_CONF_PATH='"+lv_conf_path+"'"])

