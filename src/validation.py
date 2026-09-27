import pandas as pd
import pandera.pandas as pa

schema = pa.DataFrameSchema({
    "customer_id": pa.Column(
        int,
        unique=True
    ),

    "age": pa.Column(
        int,
        checks=pa.Check.between(18, 100)
    ),

    "purchase_amount": pa.Column(
        float,
        checks=pa.Check.greater_than_or_equal_to(0)
    )
})

def validate_data(file_path):
    df = pd.read_csv(file_path)
    return schema.validate(df, lazy=True)


if __name__ == "__main__":
    valid_data = validate_data("data/valid_data.csv")
    print("Valid data:")
    print(valid_data)

    print("\nValidating invalid data...")

    try:
        invalid_data = validate_data("data/invalid_data.csv")
        print(invalid_data)
    except pa.errors.SchemaErrors as error:
        print("\nValidation errors:")
        print(error)
