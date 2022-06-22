.accounts | (length, (.[] | if .health > 0 then .health else empty end))
