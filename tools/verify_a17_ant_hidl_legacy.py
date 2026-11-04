#!/usr/bin/env python3
"""Source-only ANT HIDL interface inventory; does not run hidl-gen or VINTF."""
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "interfaces" / "ant"
package = (root / "Android.bp").read_text()
bp = (root / "1.0/Android.bp").read_text()
hal = (root / "1.0/IAnt.hal").read_text()
cb = (root / "1.0/IAntCallbacks.hal").read_text()
current = (root / "current.txt").read_text()
checks = {
    "legacy HIDL package root": "hidl_package_root" in package and "com.dsi.ant" in package,
    "HIDL interface 1.0 declared": 'name: "com.dsi.ant@1.0"' in bp,
    "legacy HIDL Java generation": "gen_java: true" in bp,
    "HIDL base dependency": "android.hidl.base@1.0" in bp,
    "service interface": "interface IAnt {" in hal,
    "antenna enable and disable API": "enable()" in hal and "disable()" in hal,
    "data and command transport": "sendDataMessage" in hal and "sendCommandMessage" in hal,
    "callbacks": "onMessageReceived" in cb and "onTransportDown" in cb,
    "historical interface hashes": "com.dsi.ant@1.0::IAnt" in current and "com.dsi.ant@1.0::IAntCallbacks" in current,
}
for label, passed in checks.items():
    print(f"{'PASS' if passed else 'FAIL'}: {label}")
if not all(checks.values()):
    raise SystemExit("Legacy ANT HIDL source interface inventory changed; review required.")
print("PASS: legacy interface inventory only; no actual HAL service or device was tested.")
