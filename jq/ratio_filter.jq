length,
(.accounts[] 
 | (.total_borrow_value_in_eth.value|tonumber) as $bor
 | (.total_collateral_value_in_eth.value|tonumber) as $sup
 | (if ($sup > 0) then ($bor / $sup) else 0 end) as $rat
 | if ($rat > 0) then {bor: $bor, sup: $sup, rat: $rat} else empty end
)
