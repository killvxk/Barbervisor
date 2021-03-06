# Handles generation of the `handle_serialize_named_tuple` macro in
# `tuple_gen.rs`

print("""/// AUTOGENERATED BY serialize_tuple_gen.py DO NOT MODIFY!
/// Handles serialization of tuples by accessing each field as part of a
/// different matching rule indicating the depth of the macro""")

# Maximum number of tuple fields
NUM_TUPLES_ALLOWED = 64

# Generate matches for different depths of enums
print("#[macro_export]")
print("macro_rules! handle_serialize_named_tuple {")
for num_fields in range(NUM_TUPLES_ALLOWED + 1):
    impl = "    ($self:ident, $buf:expr"
    for field_id in range(num_fields):
        impl += ", $ty%d:ty" % field_id
    impl += ") => {\n"

    for field_id in range(num_fields):
        impl += "        Serialize::serialize(&$self.%d, $buf);\n" % field_id
    impl += "    };"
    print(impl)
print("}")

