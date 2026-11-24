import { Project } from './project.model';

export const PROJECTS: Project[] = [
  {
    slug: 'construi-tu-futuro',
    title: 'Plataforma Construí tu Futuro',
    summary: 'Plataforma de orientación para el empleo con más de 40.000 personas registradas.',
    category: 'web',
    tags: ['Django', 'Angular', 'Celery', 'Moodle'],
    image: 'img/job-hunt.svg',
    caseStudy: {
      context:
        'El programa necesitaba una herramienta para que la ciudadanía evaluara sus habilidades para la empleabilidad y accediera a talleres y cursos de orientación.',
      role: 'Análisis del requerimiento y desarrollo full stack, desde la primera versión hasta su evolución a plataforma.',
      solution: [
        'Test de habilidades para la empleabilidad, integrado con Moodle para validar participantes y registrarlos automáticamente.',
        'Agenda de encuentros virtuales y presenciales con inscripción en línea.',
        'Tableros estadísticos con indicadores estratégicos y operativos.',
        'Back office para el equipo del programa, con segmentación de usuarios y exportación de datos.',
        'Procesamiento asíncrono de correos y otras tareas con Celery y Redis.',
      ],
      results: ['Más de 40.000 personas registradas.'],
      links: [
        { label: 'Test de Habilidades para la Empleabilidad', url: 'https://construitufuturo-test.bue.edu.ar/' },
        { label: 'Encuentros', url: 'https://encuentros-construitufuturo.bue.edu.ar/' },
      ],
    },
  },
  {
    slug: 'taller-de-ensamblado',
    title: 'Taller de Ensamblado',
    summary:
      'Simulación de carpintería para el navegador: armar muebles uniendo sus piezas con encastres, con telemetría de cada intento.',
    category: 'xr',
    tags: ['Unity', 'C#', 'WebGL', 'Bitácora'],
    image: 'img/building-blocks.svg',
    caseStudy: {
      context:
        'Aprender un procedimiento manual, como ensamblar un mueble, requiere práctica, y registrar cómo se resuelve cada intento permite analizar el aprendizaje. El objetivo fue sentar las bases técnicas de una simulación educativa de carpintería. Es un modelo de referencia, desarrollado sin supervisión de especialistas: las piezas, medidas y procedimientos son ilustrativos.',
      role:
        'Diseño, modelado y desarrollo de la simulación en Unity, e integración de Bitácora para la telemetría. Proyecto personal de código abierto, desarrollado con un flujo AI-first.',
      solution: [
        'Tres muebles de dificultad creciente (mesa ratona, taburete y silla) que se arman uniendo sus piezas con encastres de caja y espiga.',
        'Piezas modeladas en el editor de Unity a partir de sus formas básicas, sin herramientas de modelado externas.',
        'Ayuda visual: mientras se mantiene presionado un botón, se muestra el mueble armado.',
        'Controles con mouse o pantalla táctil, con detección automática del dispositivo.',
        'Resumen final con el resultado del armado y las uniones incorrectas.',
        'Telemetría con Bitácora: cada unión se registra indicando si es la esperada.',
      ],
      results: [
        'Versión 1 publicada y jugable en el navegador, en computadora o celular.',
        'Primera integración de Bitácora en una simulación real.',
        'Cada sesión se registra en un servidor en producción y sus métricas se pueden consultar en un tablero público.',
      ],
      nextSteps: [
        'Versión 2: uniones atornilladas, con atornillador y perforadora.',
      ],
      links: [
        { label: 'Probar la simulación (21 MB)', url: 'https://taller-de-ensamblado.netlify.app/' },
        { label: 'Ver las métricas en el tablero', url: 'https://bitacora-tablero.netlify.app/taller-ensamblado' },
        { label: 'Repositorio en GitHub', url: 'https://github.com/ChTole/taller-ensamblado' },
      ],
    },
  },
  {
    slug: 'bitacora',
    title: 'Bitácora',
    summary:
      'Package de Unity de código abierto para registrar sesiones y eventos de telemetría en simulaciones educativas.',
    category: 'xr',
    tags: ['Unity', 'C#', 'Python', 'Flask', 'REST API'],
    image: 'img/complete-the-steps.svg',
    caseStudy: {
      context:
        'Cada simulación educativa necesita registrar qué hace la persona que participa para poder analizar su aprendizaje. Sin una herramienta común, cada proyecto termina reimplementando la conexión con el servidor, el manejo de sesiones y los reintentos ante fallas de red.',
      role:
        'Diseño, desarrollo y documentación del package, del contrato con el servidor y de un servidor de prueba. Proyecto personal de código abierto, desarrollado con un flujo AI-first.',
      solution: [
        'Package instalable desde el Package Manager de Unity, con una plantilla de ejemplo que funciona sin servidor.',
        'Participación anónima con un alias asignado por el servidor (por ejemplo, "Carpincho Turquesa"), o identificada con un único dato configurable.',
        'Eventos numerados y enviados por lotes, con reintentos que no generan datos duplicados.',
        'Registro de pausas, por ejemplo al quitarse el visor, y cierre de la sesión como abandonada si la aplicación se cierra.',
        'Arquitectura desacoplada: la simulación solo registra eventos, y el servidor puede ser el simulado o uno real sin otros cambios.',
        'Contrato con el servidor documentado, con versiones, reglas de validación y una tabla de errores que define cómo reacciona el cliente.',
        'Servidor de prueba en Flask que implementa el contrato y permite simular fallas y demoras.',
      ],
      results: [
        'Versión 0.2.0 publicada, con la versión 1.1 del contrato. La instalación se probó en Ubuntu y Windows desde un proyecto vacío.',
        'Integrado en el Taller de Ensamblado y conectado a un servidor en producción.',
        'Diseñado para escritorio, navegador (WebGL) y Android: usa solo herramientas de Unity disponibles en las tres plataformas.',
      ],
      nextSteps: [
        'Almacenamiento local de eventos cuando no hay conexión.',
        'Vinculación de dispositivos con un código, sin configuración manual.',
      ],
      links: [
        { label: 'Repositorio en GitHub', url: 'https://github.com/ChTole/bitacora' },
        { label: 'Versión 0.2.0', url: 'https://github.com/ChTole/bitacora/releases/tag/v0.2.0' },
      ],
    },
  },
  {
    slug: 'bitacora-api-y-tablero',
    title: 'Bitácora API y Tablero',
    summary:
      'Servidor de telemetría y tablero público de métricas de aprendizaje para las simulaciones que usan Bitácora.',
    category: 'web',
    tags: ['Django', 'DRF', 'MongoDB', 'Angular', 'ECharts'],
    image: 'img/data.svg',
    caseStudy: {
      context:
        'Bitácora registraba lo que ocurre en cada simulación, pero faltaba dónde guardarlo y cómo convertirlo en información útil. El objetivo fue un servidor que implementara su contrato y un tablero abierto que mostrara cómo se resuelve cada simulación, sin datos personales de quienes participan.',
      role:
        'Diseño, desarrollo y despliegue del servidor y del tablero, con las decisiones de arquitectura documentadas. Proyecto personal de código abierto, desarrollado con un flujo AI-first.',
      solution: [
        'Servidor en Django y Django REST Framework que implementa el contrato de Bitácora, con claves de API guardadas como hash y límites de solicitudes.',
        'Sesiones en MongoDB: cada una es un documento con sus eventos incrustados, que se registran con una actualización atómica que descarta duplicados.',
        'Métricas calculadas con pipelines de agregación y expuestas en una API pública de solo lectura.',
        'Tablero en Angular con ECharts: evolución, comparación por mueble, dificultades frecuentes y búsqueda de sesiones por alias, con filtros por mueble, dispositivo y fechas.',
        'Gráficos con una paleta apta para daltonismo.',
        'Registro de decisiones de arquitectura (ADR) y tests automatizados.',
        'Despliegue sin costo en Render, MongoDB Atlas y Netlify.',
      ],
      results: [
        'Versión 0.1.0 en producción, recibiendo las sesiones del Taller de Ensamblado.',
        'Quien juega puede encontrar sus resultados con el alias que le asignó la simulación.',
        'Tablero con 100 en rendimiento, accesibilidad, buenas prácticas y SEO en PageSpeed (escritorio).',
      ],
      links: [
        { label: 'Ver el tablero', url: 'https://bitacora-tablero.netlify.app/' },
        { label: 'Repositorio de la API', url: 'https://github.com/ChTole/bitacora-api' },
        { label: 'Repositorio del tablero', url: 'https://github.com/ChTole/bitacora-tablero' },
      ],
    },
  },
  {
    slug: 'telemetria-y-analisis',
    title: 'Telemetría y Análisis',
    summary:
      'Plataforma que registra y analiza la telemetría de simulaciones de realidad virtual en Unity para Meta Quest.',
    category: 'xr',
    tags: ['Django', 'Angular', 'Unity', 'C#', 'MariaDB', 'Docker'],
    image: 'img/instant-analysis.svg',
    caseStudy: {
      context:
        'El Laboratorio necesitaba registrar y analizar lo que ocurre en cada simulación de realidad virtual, sin que las simulaciones de Unity dependieran de la administración y el análisis de los datos.',
      role:
        'Análisis del requerimiento y desarrollo full stack de la plataforma web y su API, y desarrollo del package de Unity que conecta cada simulación con la plataforma.',
      solution: [
        'Arquitectura desacoplada: las simulaciones en Unity y la plataforma de gestión en Angular comparten un backend en Django y se comunican solo mediante una API REST, por lo que cada parte evoluciona y se despliega por separado.',
        'API de telemetría con autenticación por dispositivo y un único punto de entrada que le entrega a la simulación todo lo necesario para iniciar una sesión.',
        'Eventos clasificados por grupo (tareas, interacciones, errores, solicitudes de ayuda, evaluaciones, entre otros), con datos propios de cada simulación y envío en lotes.',
        'Envíos tolerantes a fallos: cada evento lleva un número de secuencia que permite ordenarlos, descartar duplicados y reintentar sin perder ni repetir datos.',
        'Plataforma para instructores: gestión de cohortes y participantes (con importación por CSV), historial de sesiones y analíticas como tiempo promedio, errores registrados y evolución de la actividad.',
        'Roles con permisos diferenciados: el administrador configura la plataforma, el instructor gestiona y analiza, y el participante solo interactúa con la simulación.',
        'Package de Unity que integra cualquier simulación del Laboratorio con un proceso de configuración uniforme.',
      ],
      results: [
        'Versión inicial funcional, con API, registro de sesiones y eventos, y tablero de analíticas.',
        'Una simulación nueva se incorpora respetando el contrato de la API, sin cambios en el backend.',
      ],
    },
  },
  {
    slug: 'asistente-virtual',
    title: 'Asistente virtual',
    summary:
      'Chatbot que responde consultas de docentes sobre el uso de Moodle, con un back office para el equipo.',
    category: 'web',
    tags: ['Python', 'NLTK', 'TensorFlow', 'Moodle'],
    image: 'img/chat-bot.svg',
    caseStudy: {
      context:
        'Las personas que usan las aulas virtuales necesitaban resolver dudas sobre Moodle al instante, y el equipo de soporte necesitaba recibir las solicitudes de ayuda de forma ordenada y con contexto.',
      role:
        'Análisis del requerimiento y desarrollo full stack del chatbot y su back office (mayo a agosto de 2025).',
      solution: [
        'Chatbot que responde consultas sobre Moodle con explicaciones, instrucciones paso a paso y, en algunos casos, video tutoriales, y sugiere preguntas para continuar la consulta.',
        'Clasificación de cada consulta por intención, con registro del nivel de confianza de la predicción.',
        'Acceso a un manual de uso que se adapta según el tipo de usuario de Moodle (invitado o registrado).',
        'Canal de comentarios anónimos y, para usuarios registrados, envío de solicitudes de soporte.',
        'Back office con módulos de soporte (solicitudes con el rol y los datos de cada persona, e incorporación masiva de usuarios de Moodle por CSV), registro de interacciones, comentarios y gestión de usuarios del equipo.',
      ],
      results: [
        'Versión funcional completa, con chatbot, back office y registro de interacciones.',
        'Diseñado para que las consultas frecuentes se resuelvan al instante y las solicitudes de soporte lleguen al equipo ordenadas y con el contexto de cada persona.',
      ],
    },
  },
];