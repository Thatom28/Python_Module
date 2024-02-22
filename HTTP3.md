# Why HTTP 2.0 was developed
HTTP 2.0 was developed to fix the limitations that HTTP 1.1 had. The aim was to reduce latency by grouping the requests and responses,HTTP 2 allowed multiple requests and responses to be sent over a single connection, therefore faster data transfer and allows clients to specify priorities for their requests this minimised overhead to provide faster and efficient data transfer. Although this made websites faster, there were still limitation:

  1.It uses Tcp, which takes time to establish a connection because of the three-way handshake.
  2. It requires a new connection to be established by each client-server interaction.(set-up delay)
  3.Packet recovery was slow.
  4.It used a single TCP connection to send requests and responses
  4.head-of-line blocking
  
# HTTP 3
  1. HTTP 3 uses the QUIC tranfer protocolby using stream multiplexing, this eliminated head-of-line blocking and set-up delay fro connecctions between the clients and the server.
  2. HTTP3 reduced the time it took to set-up a connection
  3. It impoved packet loss recovery because it has a built-in mechanism for recovering lost packets. The mechanisms allows the packets to be corrected if there is an error or packet loss.
     
Summary: The main change from HTTP2 to 3 was the head-of-line blocking. HTTP3 was able to use multiple streams of connections to send requests and responses, which allows it to be more faster to respond to packet loss and to send the lost packet back. HTTP 2 used only one transimission which allowed to to recieve the respponse before sending the request again.
