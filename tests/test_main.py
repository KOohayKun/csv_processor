import pytest
from csv_processor.main import split_where_arg, split_aggregate_arg
from csv_processor.proccesor import filter_data, aggregate


def test_split_where_arg_simple_gt():
    result = split_where_arg("price>100")
    assert result == ("price", ">", "100")

def test_split_where_arg_lte():
    result = split_where_arg("price<=500")
    assert result == ("price", "<=", "500")

def test_split_aggregate_arg_avg():
    result = split_aggregate_arg("price=avg")
    assert result == ("price", "avg")

def test_split_where_arg_simple_lt():
    result = split_where_arg("rating<4.5")
    assert result == ("rating", "<", "4.5")

def test_split_where_arg_simple_eq():
    result = split_where_arg("brand=xiaomi")
    assert result == ("brand", "=", "xiaomi")

def test_split_aggregate_arg_min():
    result = split_aggregate_arg("rating=min")
    assert result == ("rating", "min")

def test_split_aggregate_arg_max():
    result = split_aggregate_arg("price=max")
    assert result == ("price", "max")

sample_data = [
    {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
    {"name": "galaxy s23 ultra", "brand": "samsung", "price": "1199", "rating": "4.8"},
    {"name": "redmi note 12", "brand": "xiaomi", "price": "199", "rating": "4.6"},
    {"name": "poco x5 pro", "brand": "xiaomi", "price": "299", "rating": "4.4"},
]

def test_filter_data_price_gt_500():
    result = filter_data(sample_data, "price", ">","500")
    names = [i["name"] for i in result]
    assert names == ["iphone 15 pro", "galaxy s23 ultra"]

def test_filter_data_brand_eq_xiaomi():
    result = filter_data(sample_data, "brand", "=", "xiaomi")
    names = [r["name"] for r in result]
    assert names == ["redmi note 12", "poco x5 pro"]

def test_filter_data_rating_lt_4_8():
    result = filter_data(sample_data, "rating", "<", "4.8")
    names = [r["name"] for r in result]
    assert names == ["redmi note 12", "poco x5 pro"]

def test_aggregate_avg_price():
    result = aggregate(sample_data, "price", "avg")
    assert result == (999 + 1199 + 199 + 299) / 4

def test_aggregate_min_rating():
    result = aggregate(sample_data, "rating", "min")
    assert result == 4.4

def test_aggregate_max_rating():
    result = aggregate(sample_data, "rating", "max")
    assert result == 4.9