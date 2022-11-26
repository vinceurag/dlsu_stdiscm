defmodule ProfileServiceElixir.Consumer do
  use GenServer
  use AMQP

  require Logger

  @exchange "accounts"
  @queue "profile_service_queue"
  @routing_key "user.profile_service"

  def start_link(args \\ []) do
    GenServer.start_link(__MODULE__, args, name: __MODULE__)
  end

  def stop(), do: GenServer.stop(__MODULE__)

  def init(_opts) do
    {:ok, conn} = Connection.open("amqp://guest:guest@localhost")
    {:ok, chan} = Channel.open(conn)
    setup_queue(chan)

    # Register the GenServer process as a consumer
    {:ok, _consumer_tag} = Basic.consume(chan, @queue)
    {:ok, chan}
  end

  def handle_info({:basic_deliver, payload, %{delivery_tag: tag, redelivered: redelivered}}, chan) do
    consume(chan, tag, redelivered, payload)
    {:noreply, chan}
  end

  def handle_info(_, chan) do
    {:noreply, chan}
  end

  defp setup_queue(chan) do
    {:ok, _} = Queue.declare(chan, @queue)
    :ok = Exchange.direct(chan, @exchange)
    :ok = Queue.bind(chan, @queue, @exchange, routing_key: @routing_key)
  end

  defp consume(chan, tag, _redelivered, payload) do
    payload = Jason.decode!(payload)
    Logger.info("ProfileService generated the user profile for: #{payload["user_email"]}")
    Basic.ack(chan, tag)
  end
end
