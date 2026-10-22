export interface ProjectLink {
  label: string;
  url: string;
}

export interface ProjectImage {
  src: string;  // ruta dentro de public/, por ejemplo 'img/ctf-home.webp'
  alt: string;
}

export interface CaseStudy {
  context: string;      // el problema o la necesidad
  role: string;         // qué hiciste vos
  solution: string[];   // qué se construyó
  results: string[];    // impacto, cifras
  nextSteps?: string[];  // próxima etapa, si la hay
  gallery?: ProjectImage[];
  links?: ProjectLink[];
}

export interface Project {
  slug: string;              // identificador para la URL: 'construi-tu-futuro'
  title: string;
  summary: string;
  category: 'web' | 'xr';    // para el filtro futuro
  tags: string[];
  image?: string;            // opcional: proyectos sin capturas publicables
  caseStudy?: CaseStudy;     // si no tiene, la tarjeta no muestra el botón
}