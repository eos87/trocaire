# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'AccionVBGLider'
        db.create_table('encuesta_accionvbglider', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ha_ayudado', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('se_acerca', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('invita_actividad', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('no_hace_nada', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('no_hace_problema', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('busca_alternativa', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('no_sabe', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('ud_previene', self.gf('django.db.models.fields.IntegerField')()),
            ('porque_no', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('encuesta', ['AccionVBGLider'])

        # Adding M2M table for field donde_buscar on 'AccionVBGLider'
        db.create_table('encuesta_accionvbglider_donde_buscar', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accionvbglider', models.ForeignKey(orm['encuesta.accionvbglider'], null=False)),
            ('buscarayuda', models.ForeignKey(orm['encuesta.buscarayuda'], null=False))
        ))
        db.create_unique('encuesta_accionvbglider_donde_buscar', ['accionvbglider_id', 'buscarayuda_id'])

        # Adding M2M table for field accion_tomar on 'AccionVBGLider'
        db.create_table('encuesta_accionvbglider_accion_tomar', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accionvbglider', models.ForeignKey(orm['encuesta.accionvbglider'], null=False)),
            ('quedebehacer', models.ForeignKey(orm['encuesta.quedebehacer'], null=False))
        ))
        db.create_unique('encuesta_accionvbglider_accion_tomar', ['accionvbglider_id', 'quedebehacer_id'])

        # Adding M2M table for field accion_prevenir on 'AccionVBGLider'
        db.create_table('encuesta_accionvbglider_accion_prevenir', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accionvbglider', models.ForeignKey(orm['encuesta.accionvbglider'], null=False)),
            ('accionprevencion', models.ForeignKey(orm['encuesta.accionprevencion'], null=False))
        ))
        db.create_unique('encuesta_accionvbglider_accion_prevenir', ['accionvbglider_id', 'accionprevencion_id'])

        # Adding model 'AccionPrevencion'
        db.create_table('encuesta_accionprevencion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('encuesta', ['AccionPrevencion'])

        # Adding model 'Organizacion'
        db.create_table('encuesta_organizacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('encuesta', ['Organizacion'])

        # Adding model 'Lider'
        db.create_table('encuesta_lider', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
            ('comunidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Comunidad'])),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Municipio'])),
            ('estado_civil', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('lugar_origen', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('asiste_iglesia', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('cual_iglesia', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('encuestador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuestador'])),
            ('contraparte', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Contraparte'])),
            ('organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Organizacion'])),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('encuesta', ['Lider'])

        # Adding model 'InformacionSocioEconomicaLider'
        db.create_table('encuesta_informacionsocioeconomicalider', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estudia', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nivel_educativo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('trabaja_fuera', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('encuesta', ['InformacionSocioEconomicaLider'])

        # Adding M2M table for field donde_trabaja on 'InformacionSocioEconomicaLider'
        db.create_table('encuesta_informacionsocioeconomicalider_donde_trabaja', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('informacionsocioeconomicalider', models.ForeignKey(orm['encuesta.informacionsocioeconomicalider'], null=False)),
            ('lugardetrabajo', models.ForeignKey(orm['encuesta.lugardetrabajo'], null=False))
        ))
        db.create_unique('encuesta_informacionsocioeconomicalider_donde_trabaja', ['informacionsocioeconomicalider_id', 'lugardetrabajo_id'])

        # Adding model 'PrevalenciaVBGLider'
        db.create_table('encuesta_prevalenciavbglider', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('piensa_existe', self.gf('django.db.models.fields.IntegerField')()),
            ('ha_vivido_vbg', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('que_tipo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('frecuencia', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('encuesta', ['PrevalenciaVBGLider'])

        # Adding M2M table for field quien on 'PrevalenciaVBGLider'
        db.create_table('encuesta_prevalenciavbglider_quien', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('prevalenciavbglider', models.ForeignKey(orm['encuesta.prevalenciavbglider'], null=False)),
            ('quien', models.ForeignKey(orm['encuesta.quien'], null=False))
        ))
        db.create_unique('encuesta_prevalenciavbglider_quien', ['prevalenciavbglider_id', 'quien_id'])

        # Changing field 'IncidenciaPolitica.satisfecha'
        db.alter_column('encuesta_incidenciapolitica', 'satisfecha', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))


    def backwards(self, orm):
        
        # Deleting model 'AccionVBGLider'
        db.delete_table('encuesta_accionvbglider')

        # Removing M2M table for field donde_buscar on 'AccionVBGLider'
        db.delete_table('encuesta_accionvbglider_donde_buscar')

        # Removing M2M table for field accion_tomar on 'AccionVBGLider'
        db.delete_table('encuesta_accionvbglider_accion_tomar')

        # Removing M2M table for field accion_prevenir on 'AccionVBGLider'
        db.delete_table('encuesta_accionvbglider_accion_prevenir')

        # Deleting model 'AccionPrevencion'
        db.delete_table('encuesta_accionprevencion')

        # Deleting model 'Organizacion'
        db.delete_table('encuesta_organizacion')

        # Deleting model 'Lider'
        db.delete_table('encuesta_lider')

        # Deleting model 'InformacionSocioEconomicaLider'
        db.delete_table('encuesta_informacionsocioeconomicalider')

        # Removing M2M table for field donde_trabaja on 'InformacionSocioEconomicaLider'
        db.delete_table('encuesta_informacionsocioeconomicalider_donde_trabaja')

        # Deleting model 'PrevalenciaVBGLider'
        db.delete_table('encuesta_prevalenciavbglider')

        # Removing M2M table for field quien on 'PrevalenciaVBGLider'
        db.delete_table('encuesta_prevalenciavbglider_quien')

        # Changing field 'IncidenciaPolitica.satisfecha'
        db.alter_column('encuesta_incidenciapolitica', 'satisfecha', self.gf('django.db.models.fields.IntegerField')())


    models = {
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.accesocontrolrecurso': {
            'Meta': {'object_name': 'AccesoControlRecurso'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'recursos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'recursos'", 'symmetrical': 'False', 'to': "orm['encuesta.Recurso']"}),
            'recursos_decide': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'recursos_decide'", 'symmetrical': 'False', 'to': "orm['encuesta.Recurso']"})
        },
        'encuesta.accionprevencion': {
            'Meta': {'object_name': 'AccionPrevencion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.accionvbg': {
            'Meta': {'object_name': 'AccionVBG'},
            'accion_tomar': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.QueDebeHacer']", 'symmetrical': 'False'}),
            'busca_alternativa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'donde_buscar': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.BuscarAyuda']", 'symmetrical': 'False'}),
            'ha_ayudado': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invita_actividad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_hace_nada': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_hace_problema': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_sabe': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'se_acerca': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'encuesta.accionvbglider': {
            'Meta': {'object_name': 'AccionVBGLider'},
            'accion_prevenir': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.AccionPrevencion']", 'null': 'True', 'blank': 'True'}),
            'accion_tomar': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.QueDebeHacer']", 'symmetrical': 'False'}),
            'busca_alternativa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'donde_buscar': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.BuscarAyuda']", 'symmetrical': 'False'}),
            'ha_ayudado': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invita_actividad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_hace_nada': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_hace_problema': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_sabe': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'porque_no': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'se_acerca': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ud_previene': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.aporta': {
            'Meta': {'object_name': 'Aporta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.asuntopublicovbg': {
            'Meta': {'object_name': 'AsuntoPublicoVBG'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'resolverse_con': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.ResolverVBG']", 'symmetrical': 'False'})
        },
        'encuesta.buscarayuda': {
            'Meta': {'object_name': 'BuscarAyuda'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.calidadatencion': {
            'Meta': {'object_name': 'CalidadAtencion'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_porque': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'no_porque2': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'propuesta': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'propuesta2': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'si_tipo': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'si_tipo2': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'valor_servicio': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.causavbg': {
            'Meta': {'object_name': 'CausaVBG'},
            'causa': ('django.db.models.fields.IntegerField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'respuesta': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'encuesta.comoafecta': {
            'Meta': {'object_name': 'ComoAfecta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'encuesta.composicionhogar': {
            'Meta': {'object_name': 'ComposicionHogar'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'cuantos_hijos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cuantos_viven': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'entre0y6': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'entre18ymas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'entre7y17': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hijos0y6': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hijos18ymas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hijos7y17': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tiene_hijos': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tiene_pareja': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'vive_con': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.ViveCon']", 'symmetrical': 'False'})
        },
        'encuesta.comunicacionasertiva': {
            'Meta': {'object_name': 'ComunicacionAsertiva'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifico': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.SolucionConflicto']", 'symmetrical': 'False'}),
            'negociacion_exitosa': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.NegociacionExitosa']", 'symmetrical': 'False'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.conceptoviolencia': {
            'Meta': {'object_name': 'ConceptoViolencia'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'respuesta': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'sobre': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'encuesta.conocimientoley': {
            'Meta': {'object_name': 'ConocimientoLey'},
            'adulto_dinero': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'adulto_relacion': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'existe_ley': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joven_case': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'joven_relacion': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'lider_religioso': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'maestro_castiga': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'maestro_relacion': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'mencione': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'padre_golpea': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'patron_acoso': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'})
        },
        'encuesta.contraparte': {
            'Meta': {'object_name': 'Contraparte'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'})
        },
        'encuesta.corresponsabilidad': {
            'Meta': {'object_name': 'Corresponsabilidad'},
            'acompanar': ('django.db.models.fields.IntegerField', [], {}),
            'arreglar_cama': ('django.db.models.fields.IntegerField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'cuidar_enfermos': ('django.db.models.fields.IntegerField', [], {}),
            'cuidar_ninos': ('django.db.models.fields.IntegerField', [], {}),
            'hacer_compras': ('django.db.models.fields.IntegerField', [], {}),
            'hacer_mandados': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ir_reuniones': ('django.db.models.fields.IntegerField', [], {}),
            'jalar_agua': ('django.db.models.fields.IntegerField', [], {}),
            'lavar': ('django.db.models.fields.IntegerField', [], {}),
            'lavar_trastes': ('django.db.models.fields.IntegerField', [], {}),
            'limpiar': ('django.db.models.fields.IntegerField', [], {}),
            'llevar_enfermos': ('django.db.models.fields.IntegerField', [], {}),
            'llevar_lena': ('django.db.models.fields.IntegerField', [], {}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'pagar_servicios': ('django.db.models.fields.IntegerField', [], {}),
            'plancar': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.creencia': {
            'Meta': {'object_name': 'Creencia'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'creencia': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.decision': {
            'Meta': {'object_name': 'Decision'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.efectovbg': {
            'Meta': {'object_name': 'EfectoVBG'},
            'afecta_mujeres': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'como_afecta': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.ComoAfecta']", 'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.encuestador': {
            'Meta': {'object_name': 'Encuestador'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_completo': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'})
        },
        'encuesta.espacio': {
            'Meta': {'object_name': 'Espacio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.expresionvbg': {
            'Meta': {'object_name': 'ExpresionVBG'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maneras': ('django.db.models.fields.IntegerField', [], {}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'respuesta': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'encuesta.hombre': {
            'Meta': {'object_name': 'Hombre'},
            'asiste_iglesia': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'comunidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'contraparte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Contraparte']"}),
            'cual_iglesia': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'encuestador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuestador']"}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar_origen': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'encuesta.incidenciapolitica': {
            'Meta': {'object_name': 'IncidenciaPolitica'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'existen_mujeres': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'satisfecha': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'encuesta.informacionsocioeconomica': {
            'Meta': {'object_name': 'InformacionSocioEconomica'},
            'aportan': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.Aporta']", 'symmetrical': 'False'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'donde_trabaja': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.LugarDeTrabajo']", 'symmetrical': 'False'}),
            'estudia': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'hace_dinero': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel_educativo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'trabaja_fuera': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'encuesta.informacionsocioeconomicalider': {
            'Meta': {'object_name': 'InformacionSocioEconomicaLider'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'donde_trabaja': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.LugarDeTrabajo']", 'null': 'True', 'blank': 'True'}),
            'estudia': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel_educativo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'trabaja_fuera': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'encuesta.justificacionvbg': {
            'Meta': {'object_name': 'JustificacionVBG'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'justificacion': ('django.db.models.fields.IntegerField', [], {}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'respuesta': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'encuesta.lider': {
            'Meta': {'object_name': 'Lider'},
            'asiste_iglesia': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'comunidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'contraparte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Contraparte']"}),
            'cual_iglesia': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'encuestador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuestador']"}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar_origen': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Organizacion']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'encuesta.lugardetrabajo': {
            'Meta': {'object_name': 'LugarDeTrabajo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.motivoparticipacion': {
            'Meta': {'object_name': 'MotivoParticipacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.mujer': {
            'Meta': {'object_name': 'Mujer'},
            'asiste_iglesia': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'comunidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'contraparte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Contraparte']"}),
            'cual_iglesia': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'encuestador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuestador']"}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar_origen': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'encuesta.negociacionexitosa': {
            'Meta': {'object_name': 'NegociacionExitosa'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'encuesta.organizacion': {
            'Meta': {'object_name': 'Organizacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'encuesta.participacionpublica': {
            'Meta': {'object_name': 'ParticipacionPublica'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'espacio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.Espacio']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.MotivoParticipacion']", 'symmetrical': 'False'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.prevalenciavbg': {
            'Meta': {'object_name': 'PrevalenciaVBG'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'frecuencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ha_vivido_vbg': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'que_tipo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quien': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.Quien']", 'null': 'True', 'blank': 'True'})
        },
        'encuesta.prevalenciavbghombre': {
            'Meta': {'object_name': 'PrevalenciaVBGHombre'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'frecuencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ha_vivido_vbg': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'que_tipo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quien': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.Quien2']", 'null': 'True', 'blank': 'True'})
        },
        'encuesta.prevalenciavbglider': {
            'Meta': {'object_name': 'PrevalenciaVBGLider'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'frecuencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ha_vivido_vbg': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'piensa_existe': ('django.db.models.fields.IntegerField', [], {}),
            'que_tipo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quien': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.Quien']", 'null': 'True', 'blank': 'True'})
        },
        'encuesta.quedebehacer': {
            'Meta': {'object_name': 'QueDebeHacer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.quien': {
            'Meta': {'object_name': 'Quien'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.quien2': {
            'Meta': {'object_name': 'Quien2'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.recurso': {
            'Meta': {'object_name': 'Recurso'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'encuesta.resolvervbg': {
            'Meta': {'object_name': 'ResolverVBG'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.situacionvbg': {
            'Meta': {'object_name': 'SituacionVBG'},
            'conoce_hombres': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'conoce_mujeres': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.solucionconflicto': {
            'Meta': {'object_name': 'SolucionConflicto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'encuesta.tomadecision': {
            'Meta': {'object_name': 'TomaDecision'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'decision': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.Decision']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.vivecon': {
            'Meta': {'object_name': 'ViveCon'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'lugar.comunidad': {
            'Meta': {'object_name': 'Comunidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['encuesta']
