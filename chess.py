import chess

board = chess.Board()

board.push_san("e4")
board.push_san("e5")
board.push_san("Qh5")
board.push_san("Nc6")
board.push_san("Bc4")
board.push_san("Nf6")
board.push_san("Qxf7")

if board.is_checkmate():
    print("Scholar's Mate!")
else:
    print("The Scholar's Mate did not work.")
