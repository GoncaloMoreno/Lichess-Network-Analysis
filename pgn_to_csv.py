from converter.pgn_data import PGNData

pgn_data = PGNData('lichess_db_standard_rated_2016-04.pgn')
pgn_data.export(moves_required=False)