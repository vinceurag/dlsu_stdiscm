defmodule ProfileServiceElixir do
  @moduledoc """
  Module that handles the profile service
  """

  alias ProfileServiceElixir.Consumer

  @doc """
  Starts the profile service consumer manually.
  """
  def start_consumer() do
    Consumer.start_link()
  end

  @doc """
  Stops the profile service consumer manually.
  """
  def stop_consumer() do
    Consumer.stop()
  end
end
