# P2 — archived ANT HIDL interface: AOSP17 PE-Reborn / mondrian

**Date:** 2026-11-04. **Status:** source-only interface inventory; **NOT enabled in AOSP17**. No HIDL generation, native compilation, VINTF or radio validation on mondrian has occurred.

## Pinned HIDL surface

- Archive: [external_ant-wireless_hidl](https://github.com/PixelExperience-Reborn/external_ant-wireless_hidl/tree/seventeen), `seventeen` revision `0ee5afff121f9a5172dc8188e49244a592b31fba`.
- `interfaces/ant/Android.bp` declares a custom `hidl_package_root` at `external/ant-wireless/hidl/interfaces/ant`. `interfaces/ant/1.0/Android.bp` declares `hidl_interface` `com.dsi.ant@1.0`, `gen_java: true`, with a dependency on `android.hidl.base@1.0`.
- `IAnt.hal` supplies `getProperties`, `setCallbacks`, `enable`, `disable`, `sendDataMessage` and `sendCommandMessage`; `IAntCallbacks.hal` supplies one-way reception and transport-failure callbacks. `current.txt` pins the historical HIDL interface hashes.
- This repository contains **interface declarations**, not a device-specific implementation of `com.dsi.ant@1.0::IAnt/default`. The [legacy ANT client](https://github.com/PixelExperience-Reborn/external_ant-wireless_ant_client/blob/audit/a17-mondrian-ant-client-20261104/docs/ANDROID_17_MONDRIAN_ANT_CLIENT_AUDIT.md) declares `optional="false"` for that HIDL service in its compatibility matrix and expects an external implementation. Mere interface code cannot satisfy VINTF or power a radio.
- The owned Lineage-based [mondrian device](https://github.com/LF52406/mondrian_android_device_xiaomi_mondrian/blob/lineage-24.0/device.mk) and [sm8450-common](https://github.com/LF52406/mondrian_android_device_xiaomi_sm8450-common/blob/lineage-24.0/common.mk) reference trees do not request this ANT interface stack. They are not finished native PE-Reborn device trees.

## Safe AOSP17 decision

1. **Do not add this archive to the opt-in AOSP17 manifest**, Java static libraries, framework compatibility matrix or VINTF requirements.
2. Only if the real mondrian radio/firmware and matching vendor HAL are demonstrated, establish the exact service instance, binder transport, ownership, licensing, SELinux policy and VINTF declaration. An Android17-native interface design may be preferable to resurrecting unsupported old HIDL glue; make that choice based on tested consumers.
3. Test HAL service registration, VINTF compatibility, system/vendor interface stability, binder permissions, Java/native ABI and real ANT traffic on device. Run a relevant full Android17 build and CTS/VTS before allowing it into product packaging.

## Verification

- `tools/verify_a17_ant_hidl_legacy.py` inventories legacy `hidl_interface`, HIDL methods and hash records. It **does not run hidl-gen or prove HAL registration**.
- `seventeen` remains unchanged. Status: **inactive / hardware not demonstrated**.
