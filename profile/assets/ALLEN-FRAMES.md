# Where the Allen pictures come from

`allen-hero.jpg` and `allen-dusk.gif` were drawn by Allen's own code, not photographed and not mocked up. They are not pictures of the iMac's screen.

- Code: [aienos-mv `native/kernel/ui`](https://github.com/aien-dev/aienos-mv/tree/903277b7ac5862d531fb5d6c00f0e66e7ef7cdb0/native/kernel/ui) at commit `903277b7ac5862d531fb5d6c00f0e66e7ef7cdb0` (branch `feat/goodbye-event-horizon`).
- Test: `native/kernel/ui/tests/allen_ui_test.c` (script `scripts/ck_allen_ui_test.sh`) runs the window at 3840 by 2160 on a host computer and writes pictures. It passed with 98 checks when these were made, on 2026-10-19.
- `allen-hero.jpg` is the test's `allen-4-answer.png` (Allen after a typed "Hello Allen"), scaled to 1600 by 900. A fresh render matched the earlier file byte for byte, so the picture is repeatable.
- `allen-dusk.gif` is 43 frames of the test's dusk (the goodbye animation), one every 100 ms of the animation's own clock, scaled to 560 by 315 and played at 10 frames per second, so it runs at the speed the dusk is drawn. To get the frames, a copy of the test was changed to write a picture each 100 ms; the whole change is:

```
+        unsigned dump_next = 0;                                   (before the dusk loop)
+            if (dir && d / 100 >= dump_next) {                    (inside it, after the frame is drawn)
+                snprintf(path, sizeof path, "%s/dusk-%03u.png", dir, dump_next);
+                png(path, fb, W, 1, 0, 0, W, H, 3);
+                dump_next++;
+            }
```

Nothing was retouched. The dusk has run on a host computer only, not on the real iMac.
