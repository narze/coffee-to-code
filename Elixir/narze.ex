# Usage: elixir Elixir/narze.ex

input = "Coffee"

output =
  input
  |> String.split("")
  |> Enum.reverse()
  |> Enum.map(fn char ->
    case char do
      "C" -> "e"
      "o" -> "d"
      "f" -> "o"
      _ -> "C"
    end
  end)
  |> Enum.uniq()
  |> Enum.join()

"Input: #{input}" |> IO.puts()
"Output: #{output}" |> IO.puts()
