import { Component, computed, inject, input } from '@angular/core';
import { ProjectService } from '../../core/project-service';
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
 
  protected readonly project = computed(() => this.projectService.getBySlug(this.slug()));
}
