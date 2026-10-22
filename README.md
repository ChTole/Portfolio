# Christian Ariel Toledo – Portfolio

**Desarrollador Full Stack | Python · Django · Angular | Plataformas educativas y telemetría para XR con Unity**

Portfolio personal con mis proyectos de desarrollo web, análisis de datos y simulación en Unity.

🔗 **Sitio publicado:** [christiantoledo-dev.netlify.app](https://christiantoledo-dev.netlify.app)

## Tecnologías

- [Angular](https://angular.dev/) 22
- [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) 5.3
- CSS

## Ejecución local

Requisitos: [Node.js](https://nodejs.org/es/download) en una versión compatible con Angular 22.

```bash
git clone https://github.com/ChTole/Portfolio.git
cd Portfolio
npm install
npm start
```

Luego abrir `http://localhost:4200/` en el navegador.

## Estructura

```
src/
├── app/
│   ├── core/          # Servicios globales (por ejemplo, idioma)
│   ├── shared/        # Componentes reutilizables: navbar, footer, tarjeta de proyecto
│   ├── pages/
│   │   ├── home/            # Página principal
│   │   └── project-detail/  # Caso de estudio de cada proyecto
│   └── data/          # Contenido de los proyectos
└── assets/
    ├── cv/            # CV descargable (castellano e inglés)
    └── img/           # Imágenes y capturas
```

## Hoja de ruta

- [x] **MVP 1:** Página principal, CV descargable y proyectos destacados.
- [x] **MVP 2:** Casos de estudio de los proyectos web.
- [ ] **MVP 3:** Simulador de ensamblado de muebles en Unity (WebGL), embebido en el portfolio.
- [ ] **MVP 4:** Telemetría del simulador: backend en Django y tablero de métricas.