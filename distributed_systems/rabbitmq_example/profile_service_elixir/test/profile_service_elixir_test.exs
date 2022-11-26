defmodule ProfileServiceElixirTest do
  use ExUnit.Case
  doctest ProfileServiceElixir

  test "greets the world" do
    assert ProfileServiceElixir.hello() == :world
  end
end
