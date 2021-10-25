-- run at: https://onecompiler.com/lua/3xfev9pgf
local function translate(s)
  local t = {}
  local e = 0
  for c in string.gmatch(s, ".") do
    if c == "f" then goto c end
    if c == "e" and e ~= 1 then e = e + 1; table.insert(t, "d"); goto c end
    table.insert(t, c)
    ::c::
  end
  return table.concat( t, "")
end

print(translate("coffee")) --> "code"