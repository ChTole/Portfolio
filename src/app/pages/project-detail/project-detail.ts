import { Component, computed, effect, inject, input } from '@angular/core';
import { ProjectService } from '../../core/project-service';
import { Title } from '@angular/platform-browser';
import { PROFILE } from '../../data/profile';
import { RouterLink } from '@angular/router';

@Component({
  imports: [RouterLink],
  selector: 'app-project-detail',
  styleUrl: './project-detail.css',
  templateUrl: './project-detail.html',
})
export class ProjectDetail {
  slug = input.required<string>();
 
  private readonly projectService = inject(ProjectService);
  private readonly title = inject(Title);
 
  protected readonly project = computed(() => this.projectService.getBySlug(this.slug()));
 
  constructor() {
    effect(() => {
      const project = this.project();
      this.title.setTitle(project ? `${project.title} | ${PROFILE.name}` : PROFILE.name);
    });
  }
}
