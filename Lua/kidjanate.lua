-- Usage `lua Lua/kidjanate.lua` or run from VSCode with Lua debug extension.

local function GetCode()
    local Coffee = "Coffee"
    local Code = ""
    for c in Coffee:gmatch"." do
        if Code:len() == 0 then Code = Code .. c else
            local chrToAdd = ""
            if Code:sub(Code:len(), Code:len()) == string.char(111) then
                chrToAdd = string.char(100)
            else
                chrToAdd = c
            end
            Code = Code .. chrToAdd
        end
    end
    Code = Code:sub(0,3) .. Code:sub(5,5)
    return Code
end

print(GetCode())