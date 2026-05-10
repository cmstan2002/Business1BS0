#!/bin/bash
set -u

ARCHIVE_DIR="/Users/chris/STUDY/edexcel_gscs_business_1bs0_archive"
RAW_DIR="$ARCHIVE_DIR/raw_downloads"
URLS_FILE="$ARCHIVE_DIR/logs/download_urls.txt"
LOG_FILE="$ARCHIVE_DIR/logs/download_log.txt"

mkdir -p "$RAW_DIR"
: > "$LOG_FILE"

ok=0
fail=0
total=0

while IFS= read -r url; do
  # skip blank lines and comments
  case "$url" in ''|\#*) continue ;; esac
  total=$((total+1))
  fname="$(basename "$url" | sed 's/%20/_/g')"
  out="$RAW_DIR/$fname"
  if [ -s "$out" ]; then
    echo "SKIP (exists): $fname" | tee -a "$LOG_FILE"
    ok=$((ok+1))
    continue
  fi
  http=$(curl -sL -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" \
    -w '%{http_code}' -o "$out" --max-time 60 "$url" 2>/dev/null)
  size=$(stat -f %z "$out" 2>/dev/null || echo 0)
  # treat <5KB or 404 as failure, also detect HTML soft-404
  is_pdf=$(head -c 4 "$out" 2>/dev/null | tr -d '\0')
  if [ "$http" = "200" ] && [ "$size" -gt 5000 ] && [ "$is_pdf" = "%PDF" ]; then
    echo "OK   ($http, ${size}B): $fname  <- $url" | tee -a "$LOG_FILE"
    ok=$((ok+1))
  else
    rm -f "$out"
    echo "FAIL ($http, ${size}B): $fname  <- $url" | tee -a "$LOG_FILE"
    fail=$((fail+1))
  fi
done < "$URLS_FILE"

echo "" | tee -a "$LOG_FILE"
echo "=== TOTAL: $total / OK: $ok / FAIL: $fail ===" | tee -a "$LOG_FILE"
