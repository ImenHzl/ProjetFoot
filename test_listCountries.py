import pytest
from listCountries import Pays

def test_PaysSpec():
    # Préparation des données de test simulées
    mock_info = ['France', 'Spain', 'Germany']
    
    # Mocking la méthode listCountries pour éviter l'appel à l'API
    with pytest.mock.patch.object(Pays, 'listCountries') as mock_list_countries:
        mock_list_countries.return_value = mock_info

        # Test avec la lettre 'F'
        result_F = Pays.PaysSpec('F')
        assert result_F == ['France']

        # Test avec la lettre 'S'
        result_S = Pays.PaysSpec('S')
        assert result_S == ['Spain']

        # Test avec la lettre 'G'
        result_G = Pays.PaysSpec('G')
        assert result_G == ['Germany']

        # Test avec une lettre qui ne correspond à aucun pays
        result_X = Pays.PaysSpec('X')
        assert result_X == []

if __name__ == '__main__':
    pytest.main([__file__])
