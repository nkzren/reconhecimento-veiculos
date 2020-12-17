# reconhecimento-veiculos
Projeto de reconhecimento de veículos criado na disciplina LabXP do IME-USP

# Pré-requisitos
- Python 3.8
- Docker

# Build

`docker build .`

# Deploy
`docker run -p 8000:8000 <image-id>`

# Reconhecimento de placa

Após subir o container, é disponibilizado um endpoint em `localhost:8000/detect`

### Formato da Entrada

```json
{
  "image": "<Codigo base64 da imagem a ser reconhecida>"
}
```

### Formato da Saída

```json
{
  "characters": "ABC1234",
  "charset": "utf-8"
  "plate_image": "<Codigo base64 da imagem da placa cortada>"
}
```
