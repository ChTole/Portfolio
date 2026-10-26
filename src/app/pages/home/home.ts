import { Component, computed, inject, signal } from '@angular/core';
import { ProjectService } from '../../core/project-service';
import { ProjectCard } from '../../shared/project-card/project-card';
import { PROFILE } from '../../data/profile';
import { SKILL_GROUPS } from '../../data/skills';
import { RouterLink } from '@angular/router';
import { SocialLinks } from '../../shared/social-links/social-links';
import { Project } from '../../data/project.model';

type ProjectFilter = 'all' | Project['category'];

@Component({
  imports: [
    RouterLink, ProjectCard, SocialLinks
  ],
  selector: 'app-home',
  styleUrl: './home.css',
  templateUrl: './home.html',
})
export class Home {
  protected readonly profile = PROFILE;
  protected readonly skillGroups = SKILL_GROUPS;

  private readonly allProjects = inject(ProjectService).getAll();

  protected readonly filters: { value: ProjectFilter; label: string }[] = [
    { value: 'all', label: 'Todos' },
    { value: 'web', label: 'Web' },
    { value: 'xr', label: 'Juegos y XR' },
  ];

  protected readonly filter = signal<ProjectFilter>('all');

  protected readonly projects = computed(() => {
    const selected = this.filter();
    return selected === 'all'
      ? this.allProjects
      : this.allProjects.filter(project => project.category === selected);
  });
}
