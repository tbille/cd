mkdir -p $XDG_RUNTIME_DIR/speech-dispatcher
$SNAP/usr/bin/speech-dispatcher -d -C "$SNAP/etc/speech-dispatcher" -S "$XDG_RUNTIME_DIR/speech-dispatcher/speechd.sock" -m "$SNAP/usr/lib/speech-dispatcher-modules"

bin/cdrom.py
