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
        'Diseño, desarrollo y documentación del package, del contrato con el servidor y de un servidor de prueba. Proyecto personal de código abierto.',
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
        'Versión 0.1.0 publicada, probada en Ubuntu y Windows con instalación desde un proyecto vacío.',
        'Diseñado para escritorio, navegador (WebGL) y Android: usa solo herramientas de Unity disponibles en las tres plataformas.',
      ],
      nextSteps: [
        'Integración en el Taller de Ensamblado, una simulación de carpintería en desarrollo.',
        'Almacenamiento local de eventos cuando no hay conexión.',
        'Vinculación de dispositivos con un código, sin configuración manual.',
      ],
      links: [
        { label: 'Repositorio en GitHub', url: 'https://github.com/ChTole/bitacora' },
        { label: 'Versión 0.1.0', url: 'https://github.com/ChTole/bitacora/releases/tag/v0.1.0' },
      ],
    },
  },
  {
    slug: 'telemetria-y-analisis',
    title: 'Telemetría y Análisis',
    summary:
      'Plataforma que registra y analiza la telemetría de simulaciones de realidad virtual en Unity para Meta Quest. Publicación pendiente.',
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
      nextSteps: [
        'Reproducción de sesiones (replay) para revisar cada experiencia paso a paso.',
        'Indicadores resumidos y nuevas métricas en el tablero y la analítica.',
      ],
    },
  },
  {
    slug: 'asistente-virtual',
    title: 'Asistente virtual',
    summary:
      'Chatbot que responde consultas de docentes sobre el uso de Moodle, con un back office para el equipo. Publicación pendiente.',
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
        'Las consultas frecuentes se resuelven al instante, y las solicitudes de soporte llegan al equipo ordenadas y con el contexto de cada persona.',
        'El registro de interacciones permite evaluar el desempeño del asistente y mejorarlo con datos reales de uso.',
      ],
      nextSteps: [
        'Tableros con visualizaciones interactivas y métricas de uso.',
        'Informes exportables.',
      ],
    },
  },
];