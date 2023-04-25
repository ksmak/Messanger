# Messanger
Messanger

Решение задачи:

...
def validate(self, data):
    if not data['is_many']:
        if len(data['members']) != 2:
            raise serializers.ValidationError(
                "Кол-во участников должно быть равно 2"
            )

    return data
