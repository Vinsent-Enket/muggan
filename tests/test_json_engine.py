from src.utils.json_engine import mask_maker


def test_mask_maker():
    assert mask_maker([]) == []