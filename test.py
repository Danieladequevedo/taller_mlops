from app import generate_a

new_data = {'pregunta': "hola"
            }

def test_answer():
    answer = generate_a(new_data)
    assert answer != ""
    print(answer)

respuesta = test_answer()