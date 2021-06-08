bootanim=""
failcounter=0
timeout_in_sec=420
echo 'Emulator is loaded'

until [[ "$bootanim" =~ "stopped" ]]; do
  bootanim=`/ui-tests/platform-tools/adb -e shell getprop init.svc.bootanim 2>&1 &`
  if [[ "$bootanim" =~ "device not found" || "$bootanim" =~ "device offline" || "$bootanim" =~ "running" ]]; then
    let "failcounter += 1"
    echo "Waiting for emulator to start"
    if [[ $failcounter -gt timeout_in_sec ]]; then
      echo "Timeout ($timeout_in_sec seconds) reached; failed to start emulator"
      exit 1
    fi
  fi
  sleep 5
done